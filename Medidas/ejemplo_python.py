from comando import comando
from func_get_signal_osc import func_get_signal_osc
import matplotlib.pyplot as plt    
import time

t,y = func_get_signal_osc('O07',1)
plt.plot(t,y)
plt.show()

comando('O07','C1:VOLT_DIV 1')
time.sleep(1)
respuesta = comando('O07','C1:Volt_DIV?')
print(respuesta)

