# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:18:40 2019

Medidas Eléctricas curso 2023
"""
#from __future__ import division, unicode_literals, print_function, absolute_import

import pyvisa as visa
from get_visa_address import get_visa_address

def comando(id,comand):
  
    visaID = get_visa_address(id)
       
    if visaID != -1:
        
        rm = visa.ResourceManager()
        instrument = rm.open_resource(visaID)
        
        instrument.read_termination = '\n'
        instrument.write_termination = '\n'
          
        if comand.find('?')!=-1:
            respuesta = instrument.query(comand)
            #print(respuesta)
            instrument.close()
            return respuesta
        else:
            instrument.write(comand)
            instrument.close()
        
    else:
        respuesta ='ERROR: el id del instrumeto no es válido'
        return respuesta
    

    
'''ejemplo de uso'''
#respuesta=comando('O06','*IDN?')
#print(respuesta)
#print(comando('O6','C1:VOLT_DIV?'))
#comando('O06','C1:VOLT_DIV 1')