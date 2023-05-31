#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time 
import numpy as np
from math import log
from matplotlib import pyplot as plt
from comando import comando
from func_get_signal_osc import func_get_signal_osc


# In[2]:


# Nombres de los dispositivos
nombre_gen = 'G01'  # Nombre del generador
nombre_osc = 'O07'  # Nombre del osciloscopi


# In[3]:


# Parámetros de frecuencia
f_min = 10  # Frecuencia mínima
f_max = 990  # Frecuencia máxima
df = 10  # Paso de frecuencia
f = np.arange(f_min, f_max + df, df)  # Vector de frecuencias

f_min = 1e3
f_max = 0.9e6
df= 1e3
f =np.concatenate((f,np.arange(f_min, f_max + df, df)))
print(np.size(f))


# In[4]:


escalas_t = np.array([5, 2, 1, 5e-1 , 2e-1, 1e-1, 5e-2 , 2e-2, 1e-2, 5e-3, 2e-3, 1e-3, 5e-4 , 2e-4, 1e-4, 5e-5 , 2e-5, 1e-5, 5e-6 , 2e-6, 1e-6,0.5e-6])
escalas_t = escalas_t[::-1]
escalas_V = np.array([50e-3, 20e-3, 10e-3, 5e-3, 2e-3,1e-3,500e-6,200e-6,100e-6,50e-6,20e-6,10e-6])
escalas_V = escalas_V[::-1]

# In[5]:


A = np.array([])  # Vector de amplitudes
Phi = np.array([])  # Vector de fases
f_osci = np.array([]) #Vector de frecuencias

# In[6]:


for freq in f:
    indice = 0
    while (10*escalas_t[indice] <= 2/freq): #Agarro la escala de tiempo que me muestre por lo menos dos peridodos de la onda
        indice = indice + 1        
    #Pongo las unidades de la frecuencia
    if freq >= 1e3:
        freq = str(int(freq/1e3)) + 'KHZ'
    else:
        freq = str(int(freq/1)) + 'HZ'
        
    #Instrucciones a el generador
    comando(nombre_gen,'BSMV WVTP, SINE ')
    comando(nombre_gen,'BSWV FRQ, '+ freq)
    comando(nombre_gen,'BSWV AMP, 1V')
    comando(nombre_gen,'BSWV PHSE, 0°')
    
    #unidades a la escala de tiempos del osciloscopio
    if escalas_t[indice] < 1:
        if escalas_t[indice] > 1e-3:
            divisionT = str(int(escalas_t[indice]*1e3)) +'MS'
        else:
            divisionT = str(int(escalas_t[indice]*1e6)) +'US'
    else:
        divisionT = str(int(escalas_t[indice])) +'S'   
    
    #Escala de tiempo al osciloscopio
    comando(nombre_osc, 'TDIV ' + divisionT)
    
    #Consulto la amplitud para ver que este bien la escala
    amplitud = comando(nombre_osc,'C1:PAVA? AMPL')[13:] #Este comando me devuelve C1:PAVA AMPL 16.00E-03MV por ejemplo
    j=0
    while amplitud[j] != 'M' or amplitud[j] != 'U' or amplitud[j] != 'V': 
        j = j + 1
    if amplitud[j] == 'M':
        amplitud = float(amplitud[13:j])*1e-3
    elif amplitud[j] == 'U':
        amplitud = float(amplitud[13:j])*1e-6
    elif amplitud[j] == 'V':
        amplitud = float(amplitud[13:j])
    j=0     
    while (amplitud >= 4*escalas_V[j]): #La amplitud no puede ser mas grande que 4 divisiones
        j = j + 1     
        
    escala_V = escalas_V[j]     #Registro la escala que necesito
    
    if escala_V < 1:
        if escala_V > 1e-3:
            escala_V = str(int(escala_V))*1e3 + 'MV'
        if escala_V < 1e-3 and escala_V > 1-6:
            escala_V = str(int(escala_V))*1e6 + 'UV'
    else:
        escala_V = str(int(escala_V)) + 'V'
        
    comando(nombre_osc,'C1:Volt_DIV '+ escala_V)
    time.sleep(4*escalas_t[indice])
    #Falta calle de aca en adelante todavia
    amplitud = 1 #comando(nombre_osc,'C1:PAVA? AMPL')
    fase = 1 #comando(nombre_osc,'C1:PAVA? PHASE')
    frecuencia = freq #comando(nombre_osc,'C1:PAVA? FREQ')
    
    #Registro la amplitud, fase y frecuencia
    A = np.append(A,amplitud)
    Phi = np.append(Phi,fase)
    f_osci = np.append(f_osci,frecuencia)
    
    


# In[7]:


print(np.size(A))


# In[10]:


#Bode
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=[5, 11])

# Plotting the graph without using loglog
ax1.loglog(f_osci, A, linestyle = 'solid', linewidth=2)
ax1.set_title('Bode de módulo', fontsize=15)
ax1.set_xlabel('20log(f)', fontsize=13)
ax1.set_ylabel('20log(A)', fontsize=13)


# Plotting the graph with Log ticks at x and y axis using loglog
ax2.loglog(f_osci, Phi, linestyle = 'solid', linewidth=2)
ax2.set_title('Bode de fase', fontsize=15)
ax2.set_xlabel('20log(f)', fontsize=13)
ax2.set_ylabel('20log(A)', fontsize=13)

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




