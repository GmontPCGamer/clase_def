import os
os.system
from funciones import *
#importar funciones de carpeta
##########################################################################################
menu()
opc = validar_opc([1,2,3,4])

if opc == 1:
    suma_2_num()
elif opc == 2:
    valor1= float(input('ingrese primer numero: '))
    valor2= float(input('ingrese segundo numero: '))
    restar_2_num(valor1, valor2)
elif opc == 3:
    total = multiplicar_2_num()
    print('el total de la multiplicación es:', total)
else:
    valor1= int(input('ingrese primer numero: '))
    valor2= int(input('ingrese segundo numero: '))
    total = dividir_2_num(valor1/valor2)
    lista = []
    lista.append(total)
    print(lista)
    