#Numero impar y par - juego
from random import randint

#Variables para ingreso inicial y ajuste de número
num1 = 0
num2 = 0
resultado1 = 0
resultado2 = 0
#Ajuste de numero
numero = 0


#Parte de adivincación
primer_intento = 0
segundo_intento = 0
tercer_intento = 0
contador_intentos = 1

print("Inicia el juego")


print("Ingrese un limite inferior")
num1 = int(input(":"))




print("Ingrese un limite superior")
num2 = int(input(":"))
if num1 > num2:
    print("El limite inferior debe ser menor que el limite superior")


numero = randint(num1, num2)
print(numero)
if numero % 2 == 0:
    numero = numero
else:
    if numero + 1 <= num2:
        numero_ajustado = numero + 1
        numero = numero_ajustado
        print(numero)
      
    else:
        numero_ajustado = numero -1
        numero = numero_ajustado
        print(numero)
       




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
        