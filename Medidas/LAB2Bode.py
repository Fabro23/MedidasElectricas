#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import numpy as np
import matplotlib.pyplot as plt
from comando import comando
from func_get_signal_osc import func_get_signal_osc

# Parámetros de frecuencia
f_min = 100  # Frecuencia mínima
f_max = 10000  # Frecuencia máxima
df = 100  # Paso de frecuencia

# Nombres de los dispositivos
nombre_gen = 'G01'  # Nombre del generador
nombre_osc = 'O07'  # Nombre del osciloscopio

# Valores de la señal del generador
A_gen = 1  # Amplitud del generador
phi_gen = 0  # Fase del generador

# Vectores de frecuencia, amplitud y fase
f = np.arange(f_min, f_max + df, df)  # Vector de frecuencias
A = []  # Vector de amplitudes
Phi = []  # Vector de fases

# Vector de escalas de tiempo en segundos
escalas_t = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005]

# Parámetros de control de escala de tiempo
Nmax = 6  # Número máximo de ciclos vistos
Nmin = 2  # Número mínimo de ciclos vistos
indice_t = 2  # Índice inicial del vector de escalas de tiempo

# Medición de amplitud y fase para cada frecuencia
for freq in f:
    # Configurar el generador
    comando(nombre_gen, 'C1:VOLT_DIV ' + str(A_gen))
    comando(nombre_gen, 'C1:FREQ ' + str(freq))
    comando(nombre_gen, 'C1:FUNC SINE')
    comando(nombre_gen, 'C1:PHASE ' + str(phi_gen))

    # Ajustar la escala de tiempo en el osciloscopio
    T = 1 / freq
    N = 10 * escalas_t[indice_t] / T

    while N > Nmax or N < Nmin:
        if N > Nmax:
            indice_t += 1
        elif N < Nmin:
            indice_t -= 1
        N = 10 * escalas_t[indice_t] / T

    tdiv = escalas_t[indice_t]
    comando(nombre_osc, 'TDIV ' + str(tdiv))
    time.sleep(1)

    # Obtener la amplitud y fase del osciloscopio
    amplitud = comando(nombre_osc, 'C1:VOLT_DIV?')
    fase = comando(nombre_osc, 'C1:PHASE?')

    # Convertir los valores a números
    amplitud = float(amplitud)
    fase = float(fase)

    # Almacenar los valores en los vectores correspondientes
    A.append(amplitud)
    Phi.append(fase)

# Convertir los vectores a numpy arrays
A = np.array(A)
Phi = np.array(Phi)

# Calcular el Bode de la transferencia
Bode_modulo = 20 * np.log10(A / A_gen)  # Bode de módulo en decibeles
Bode_fase = Phi - phi_gen  # Bode de fase

# Graficar el Bode de módulo
plt.figure()
plt.semilogx(f, Bode_modulo)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Bode de Módulo (dB)')
plt.grid(True)
plt.title('Bode de Módulo')
plt.show()

# Graficar el Bode de fase
plt.figure()
plt.semilogx(f, Bode_fase)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Bode de Fase (grados)')
plt.grid(True)
plt.title('Bode de Fase')
plt.show()

