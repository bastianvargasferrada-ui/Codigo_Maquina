#Numero impar y par - juego
from random import randint

#Variables para ingreso inicial y ajuste de número
num1 = 0
num2 = 0
resultado1 = 0
resultado2 = 0
#Parte de adivincación
primer_intento = 0
primer_Resultado = 0
segundo_intento = 0
segundo_Resultado = 0
tercer_intento = 0
contador_intentos = 1




print("Ingrese un limite inferior")
num1 = int(input(":"))
resultado1 = num1 % 2
if resultado1 == 1:
    num1 = num1 + 1


print("Ingrese un limite superior")
num2 = int(input(":"))
resultado2 = num2 % 2
if resultado2 == 1:
    num2 = num2 - 1





numero = randint(num1, num2)


print("Intentos", contador_intentos)
primer_intento = int(input("Intente adivinar: "))
if primer_intento == numero:
    print("Felicidades, has adivinado")
else:
    contador_intentos += 1
    if numero > primer_intento:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    print("Intento", contador_intentos)
    segundo_intento = int(input("Intente adivinar: "))
    if segundo_intento == numero:
        print("Felicidades has adivinado")
    else:
        contador_intentos += 1
        if numero > segundo_intento:
            print("El numero es mayor")
        else:
            print("El numero es menor")
        primer_Resultado = (primer_intento - numero)
        if primer_Resultado < 0:
            primer_Resultado *= -1
        segundo_Resultado = (segundo_intento - numero)
        if segundo_Resultado < 0:
            segundo_Resultado *= -1
        if primer_Resultado > segundo_Resultado:
            print("El número que buscas esta más cerca del", segundo_intento, "que de ", primer_intento)
        else:
            print("El número que buscas esta más cerca del", primer_intento, "que de ", segundo_intento)
        print("Intento", contador_intentos)
        tercer_intento = int(input("Intente adivinar: "))
        if tercer_intento == numero:
            print("Felicidades, has adivinado")
        else:
            print("Has perdido")
            print("El numero era ", numero)
        