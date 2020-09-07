#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Patricio D'Antonio
#
# Created:     24/10/2019
# Copyright:   (c) Patricio D'Antonio 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python



# Hacer un programa que calcule el precio a pagar de cada cliente de una panaderia
# y la cantidad de kg vendidos en el día.


def main():
    pass

if __name__ == '__main__':
    main()

A = 0
PA = "SI"
PC = 135
PS = 184
CPC = 0
CPS = 0
CT = []
VFPS = 0
VFPC = 0
TOT = 0

def FPC (PC,CPC):
    FPC = int(PC*CPC)
    return FPC

def FPS (PS,CPS):
    FPS = int(PS*CPS)
    return FPS

def MTP (FPC,FPS):
    MTP = VFPC+VFPS
    return MTP

while PA == "SI":
    CPC = int(input("Ingrese la cantidad de Kg de pan comun de esta compra: "))
    CPS = int(input("Ingrese la cantidad de Kg de pan de salvado de esta compra: "))
    VFPS = FPS(PS,CPS)
    VFPC = FPC(CPC,PC)
    CT.append(CPC+CPS)
    print("El monto de este cliente es de: $", MTP(FPC,FPS))
    A = A+1
    PA = str(input("Desea ingresar otra compra? Si/No"))
    PA = PA.upper()

for I in range (0,len(CT)):
    TOT = TOT+CT[I]

print("El total de Kg vendidos fue: ", TOT)














