#Rango Númerico

contador_intentos = 0
primer_intento = 0
primer_Resultado = 0
segundo_intento = 0
segundo_Resultado = 0
Tercer_intento = 0

from random import randint

num1 = int(input("Ingrese el limite inferior: "))
num2 = int(input("Ingrese el limite superior: "))
if num1 > num2:
    print("Valor del limite inferior invalido")
else:
    numero = randint(num1, num2)
    
    if numero % 3 != 0:
        numero_ajustado = (numero//3)*3
        numero = numero_ajustado
        
    else:
        numero
    
    print(numero)

    primer_intento = int(input("Intente adivinar: "))
    if primer_intento == numero:
        print("Felicidades, has adivinado")
    else:
        contador_intentos += 1
        if numero > primer_intento:
            print("El numero es mayor")
        else:
            print("El numero es menor")
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
                Tercer_intento = int(input("Intente adivinar: "))
                if Tercer_intento == numero:
                    print("Felicidades, has adivinado")
                else:
                    print("Has perdido")
                    print("El numero era ", numero)
        

            
    

