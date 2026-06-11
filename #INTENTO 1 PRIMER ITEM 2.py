#INTENTO 1 PRIMER ITEM 2

from random import randint

comando = ""
#Variables generales
num1 = 0
num2 = 0
numero = 0
#Ajuste
Ajuste = 0
#Vatiables del juego
intento1 = 0
intento2 = 0
intento3 = 0
resultado1 = 0
resultado2 = 0



print("Ingrese el limite inferior: ")
num1 = int(input(":"))
print("Ingrese el limite superior")
num2 = int(input(":"))
if num1 > num2:
    print("El primer numero ingresado debe ser mayor que el segundo")
numero = randint(num1, num2)
print(numero)
if numero % 3 != 0:
    Ajuste = (numero // 3) * 3
    numero = Ajuste
    
    if numero < num1:
        numero = num1
        
    elif numero > num2:
        numero = num2
        
else:
    numero
print(numero)

intento1 = int(input("Pruebe un numero: "))
if intento1 == numero:
    print("Felicidades")
elif intento1 != numero:
    if numero > intento1:
        print("El numero es mayor")
    elif numero < intento1:
        print("El numero es menor")
    intento2 = int(input("Pruebe de nuevo: "))
    if intento2 == numero:
        print("Felicidades")
    elif intento2 != numero:
        if numero > intento2:
            print("El numero es mayor")
        elif numero < intento2:
            print("El numero es menor")
        
        resultado1 = (numero - intento1)
        if resultado1 < 0:
            resultado1 = resultado1 * -1
        resultado2 = (numero - intento2)
        if resultado2 < 0:
            resultado2 = resultado2 * -1


        if resultado1 < resultado2:
            print("El numero buscado esta más cerca de", intento1, "que del", intento2)
        elif resultado1 > resultado2:
            print("El numero buscado esta más cerca de",intento2, "que del", intento1)
    intento3 = int(input("pruebe un numero: "))
    if intento3 == numero:
        print("Felicidades")
    else:
        print("perdiste")
        print("El numero era ", numero)            
    
        
        
