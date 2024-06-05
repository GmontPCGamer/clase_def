
def suma_2_num ():
    valor1 = validar_num()
    valor2 = validar_num()
    total = valor1+valor2
    print('FUNCION:El total de la suma es:', total)
def restar_2_num(p_valor1: float, p_valor2: float):
    total = p_valor1-p_valor2
    print("FUNCION: el total de la resta es:",total)
def multiplicar_2_num():
    valor1 = validar_num()
    valor2 = validar_num()
    total = valor1*valor2
    return total

def dividir_2_num(p_valor1:int,p_valor2:int):
    total = p_valor1/p_valor2
    return total

def validar_num():
    while True:
        try:
            num = float(input('ingrese numero: '))
            break
        except:
            print('ERROR DEBE INGRESAR UN NUMERO ENTERO')
    return num 

def menu():
    print (""">>>menu<<<
        1) Sumar 2 números
        2) restar 2 num
        3) multiplicar 2 num
        4) dividir 2 num """)
def validar_opc(opciones):
    while True:
        try:
            opc = int(input("ingrese opción: "))
            if opc in opciones:
                break
            else:
                print("ERROR DEBE SER UNA OPCIÓN")
        except:
            print("ERROR DEBE SER UN NUMERO ENTERO")
    return opc