#Para usar en el canal 1


from comando import comando
from func_get_signal_osc import func_get_signal_osc
import matplotlib.pyplot as plt    
import time

#Configuro el generador de ondas
idg = 'O07' #Aca va el id del generador;
comando(idg, 'BSWV FRQ, 1KHZ') #1kHz
comando(idg, 'BSWV AMP, 3V') #6Vpp


ido = 'O06' #Id del osciloscopio
#Escala
comando(ido, 'TDIV 250US') #250us
comando(ido, 'C1:Volt_DIV 1V') #1V/div
#Trigger
comando(ido, 'TRIG_DELAY 0S') #0s delay
comando(ido, 'TRIG_MODE NORM') #Modo normal
comando(ido, 'TRIG_SELECT EDGE, SR, C1') #Elijo edge y C1


#Nivel de 0V
comando(ido, 'C1:TRIG_LEVEL 0V')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Nivel de 3V
comando(ido, 'C1:TRIG_LEVEL 3V')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Nivel de 3.5V
comando(ido, 'C1:TRIG_LEVEL 3.5V')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Set to 50%
comando(ido,'SET50')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Cambio la base de tiempo
comando(ido, 'TDIV 5US') #5us


#Nivel de 0V
comando(ido, 'C1:TRIG_LEVEL 0V')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Nivel de 3V
comando(ido, 'C1:TRIG_LEVEL 3V')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Nivel de 3.5V
comando(ido, 'C1:TRIG_LEVEL 3.5V')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Set to 50%
comando(ido,'SET50')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Parte 8
comando(ido, 'TRIG_MODE AUTO') #Modo auto
comando(idg, 'BSWV FRQ, 2HZ') #2Hz
comando(ido, 'TDIV 1S') #1s la escala de tiempo, se deberian ver dos periodos
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()


#Parte 9
comando(idg, 'BSWV FRQ, 4MHZ') #4MHz
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()

#Cambio la escala del tiempo
comando(ido, 'TDIV 125NS')
delay(1000)
t,y = func_get_signal_osc('ido',1)
plt.plot(t,y)
plt.show()

