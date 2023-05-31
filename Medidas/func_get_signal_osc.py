# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:18:40 2019

Medidas Eléctricas curso 2023
"""
#from __future__ import division, unicode_literals, print_function, absolute_import

from get_visa_address import get_visa_address
import numpy as np
import pyvisa as visa

def func_get_signal_osc(id,CH):
   
  
    resource_name = get_visa_address(id);
     
    rm = visa.ResourceManager()
    osc = rm.open_resource(resource_name)
    
    osc.read_termination = '\n'
    osc.write_termination = '\n'
    
    print(osc.query('*IDN?')) #anda
    AMPL = (osc.query('C'+str(CH)+':PAVA? AMPL')) #anda
    AMPL=float(AMPL[13:-1])
    print('AMPLitud: ',AMPL, 'V')
    #Hallar y del waveform----------------------------------------------------------
    VDIV = osc.query('C'+str(CH)+':VOLT_DIV?')
    print(VDIV)
    VDIV=float(VDIV[8:-1])
    print('Volts por DIVisión: ',VDIV, 'V')
    OFST = osc.query('C'+str(CH)+':OFST?') 
    OFST=float(OFST[8:-1])
    print('OFfSeT: ',OFST,'V')
    
    #-------------------------------------------------------------------------------
    
    #Hallar t del waveform----------------------------------------------------------
    TRDL = osc.query('TRDL?') #TRigger DeLay
    E=TRDL[-2:]
    TRDL=TRDL[4:-2]
    
    if E.find('ns'):
        TRDL=float(TRDL)*1e-9
    elif E.find('us'):
        TRDL=float(TRDL)*1e-6
    elif E.find('ms'):
        TRDL=float(TRDL)*1e-3
    else:
        TRDL=float(TRDL)
        
        
    TDIV = osc.query('TDIV?')
    TDIV = float(TDIV[5:-1]) 
    
    # T1=TRDL-TDIV*8
        
    SARA = osc.query('SARA?')
    E=SARA[-3:]
    SARA=SARA[5:-3];  
    
    if E.find('GSa'):
        SARA=float(SARA)*1e9
    elif E.find('MSa'):
        SARA=float(SARA)*1e6
    elif E.find('KSa'):
        SARA=float(SARA)*1e3
    else:
        SARA=float(SARA)
        
    DT=1/SARA
    
    #Vectores ------------------------------------
    a = np.array(osc.query_binary_values('C'+str(CH)+':WF? DAT2', datatype='b')) #'b' parece ser equivalente a int8
    y = (a*(VDIV/25))-OFST
    
    t = np.arange(0, DT*len(y), DT)
    t= t - t[round(len(t)/2)] - TRDL;    
    osc.close()
    return t,y
    #-------------------------------------------------------------------------------
    
    osc.close()
    
    
'''Ejemplo de uso'''
#from matplotlib import pyplot as plt    
#t,y = func_get_signal_osc('O06',1)
#plt.plot(t,y)