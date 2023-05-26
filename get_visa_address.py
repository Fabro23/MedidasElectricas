# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:26:47 2023

@author: Medidas Eléctricas
"""

def get_visa_address(id):
    AddressList=['O01|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5570::0::INSTR',
        'O02|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5571::0::INSTR',
        'O03|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5573::0::INSTR',
        'O04|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5572::0::INSTR',
        'O05|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5559::0::INSTR',
        'O06|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5583::0::INSTR',
        'O07|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5582::0::INSTR',
        'O08|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5584::0::INSTR',
        'O09|USB0::0xF4EC::0xEE3A::SDS1MDBQ1R5585::0::INSTR',
        'O10|USB0::0xF4EC::0xEE3A::SDS1MJGQ6R5689::0::INSTR',
        'O11|USB0::0xF4EC::0xEE3A::SDS1MJGQ6R5682::0::INSTR',
        'G01|USB0::0xF4ED::0xEE3A::SDG08BAC1L1931::0::INSTR',
        'G02|USB0::0xF4ED::0xEE3A::SDG08BAC1L1928::0::INSTR',
        'G03|USB0::0xF4ED::0xEE3A::SDG08BAC1L1929::0::INSTR',
        'G04|USB0::0xF4ED::0xEE3A::SDG08BA3161530::0::INSTR',
        'G05|USB0::0xF4ED::0xEE3A::SDG08BAC1L2228::0::INSTR',
        'G06|USB0::0xF4ED::0xEE3A::SDG08BAC1L2227::0::INSTR',
        'G07|USB0::0xF4ED::0xEE3A::SDG08BAC1L2226::0::INSTR',
        'G08|USB0::0xF4ED::0xEE3A::SDG08BAC1L1974::0::INSTR',
        'G09|USB0::0xF4ED::0xEE3A::SDG08BAC1L1930::0::INSTR',
        'G10|USB0::0xF4EC::0x1103::SDG1XCBQ6R6946::0::INSTR',
        'G11|USB0::0xF4EC::0x1103::SDG1XCBQ6R6949::0::INSTR',
        'M01|USB0::0xF4EC::0x1203::SDM34FBQ6R2126::0::INSTR',
        'M02|USB0::0xF4EC::0x1203::SDM34FBQ6R2084::0::INSTR',
        'M03|USB0::0xF4EC::0x1203::SDM34FBQ6R2125::0::INSTR',
        'M04|USB0::0xF4EC::0x1203::SDM34FBX6R0777::0::INSTR',
        'M05|USB0::0xF4EC::0x1203::SDM34FBX6R0779::0::INSTR',
        'M06|USB0::0xF4EC::0x1203::SDM34FBQ6R2083::0::INSTR',
        'M07|USB0::0xF4EC::0x1203::SDM34FBX6R0780::0::INSTR',
        'M08|USB0::0xF4EC::0x1203::SDM34FBX6R0778::0::INSTR',
        'F01|----------------------------------------------',#no esta y por eso no se sabe la direccion
        'F02|USB0::0x0483::0x7540::SPD3ECAQ1R1848::0::INSTR',
        'F03|----------------------------------------------',#no esta y por eso no se sabe la direccion
        'F04|USB0::0x0483::0x7540::SPD3ECAQ1R1845::0::INSTR',
        'F05|----------------------------------------------',#no esta y por eso no se sabe la direccion
        'F06|USB0::0x0483::0x7540::SPD3ECAC1L1225::0::INSTR',
        'F07|USB0::0x0483::0x7540::SPD3ECAQ1R1846::0::INSTR',
        'F08|USB0::0x0483::0x7540::SPD3ECAQ1R1847::0::INSTR',
        'F09|USB0::0x0483::0x7540::SPD3ECAQ1R1845::0::INSTR',
        'F10|USB0::0x0483::0x7540::SPD3EEEC6R0781::0::INSTR',
        'F11|USB0::0x0483::0x7540::SPD3EEEX6R1116::0::INSTR',    
        ]
    # Chequea el id y asisgna la direccion visa
    visaID=-1,
    for k in AddressList:
        if k.find(id)!=-1:
            visaID=k[4:]
            break
    return visaID

