#Números pares e impares

Número = 0
Resultado = 0
contador_pares = 0
contador_impares = 0

while True:
    Número = int(input("Ingrese un número: "))
    if Número == -1:
        print("Saliendo...")
        break
    Resultado = (Número % 2)
    if Resultado == 0:
        print("El número es par")
        contador_pares += 1
        
    else:
        print("El número es impar")
        contador_impares += 1
print("La cantidad de números pares ingresados es: ", contador_pares)
print("La cantidad de números impares ingresados es: ", contador_impares)