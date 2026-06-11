#SEGUNDO INTENTO ITEM2
from random import randint
num1 = 0
num2 = 0
numero = 0
#Ajuste
Ajuste = 0

print("Ingrese el limite inferior")
num1 = int(input(":"))
print("Ingrese el limite superior")
num2 = int(input(":"))

if num1 > num2:
    print("El primer numero ingresado debe ser menor que el segundo")

numero = randint(num1, num2)
if numero % 2 != 0:
    if numero + 1 > num2:
        Ajuste = numero -1
        numero = Ajuste
        print(numero)
    elif numero + 1 < num2:
        Ajuste = numero + 1
        numero = Ajuste
        print(numero)
else:
    numero = numero
print(numero)