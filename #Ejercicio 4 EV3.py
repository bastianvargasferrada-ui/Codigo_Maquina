#Ejercicio 4 EV3 


#Variables generales
#Maximo y minimo de largo de caracteres
MAX_LARGO = 16
MIN_LARGO = 8
#Minimo de numeros
MIN_NUM = 1
#Maximo caracteres especiales
MAX_ESPECIALES = 1
ESPECIALES = "-_*.!?#$%"
#Maximo espacios
MAX_ESPACIO = 0

def validar_largo(contraseña):
    if MAX_LARGO < len(contraseña):
        print("Has excedido la cantidad de caracteres permitidos\n(Maximo de caracteres: 16)")
        return True
    elif MIN_LARGO > len(contraseña):
        print("Cantidad de caracteres insuficientes\n (Minimo de caracteres: 8)")
        return True
    else:
        return False

def Validación_ultima_letra(contraseña):
    Ultima_letra = contraseña[-1]
    if Ultima_letra in ESPECIALES:
        return True
    else:
        return False

def Validar(contraseña):
    contador_num = 0
    contador_especial = 0
    contador_espacio = 0
    for caracter in contraseña:
        if caracter.isdigit():
            contador_num += 1
        if caracter in ESPECIALES:
            contador_especial += 1
        if caracter.isspace():
            contador_espacio += 1

    if (contador_num <= MIN_NUM) or (contador_especial >= MAX_ESPECIALES) or (contador_espacio > MAX_ESPACIO):
        return True
    else:
        return False
            
while True:
    print("Ingrese una contraseña:")
    contraseña = input(":")
    if validar_largo(contraseña) or Validar(contraseña) or Validación_ultima_letra(contraseña):
        print("Contraseña Invalida")
    else:
        print("Contraseña válida")
        break
    



    






