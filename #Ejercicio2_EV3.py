#Ejercicio 2

import time

usuarios = {

}
Max_usuarios = 3

def Ingreso_datos(usuarios):
    nombre = ""
    Edad = 0
    print("|== Ingreso de datos ==|")
    print("Ingrese un nombre: ")
    nombre = input(":")
    while True:
        try:
            print()
            print("Ingrese edad")
            Edad = int(input(":"))
            usuarios[nombre] = {
            "Edad": Edad
        }
            
            return usuarios

        except ValueError:
            print("Solo pueden ser numeros")
            return True
        

def calculo_promedio():
    print()
    suma_edades = 0
    promedio = 0
    for usuario in usuarios.values():
        suma_edades += usuario["Edad"]
    promedio = suma_edades//len(usuarios)
    print("| Promedio |")
    print("El promedio de edades es de ", promedio)
    
    



            





def Menu():
    print()
    opc = 0
    contador_usuarios = 0
    while opc != 3:
        print()
        print("|== Menu ==|")
        print("1) Crear usuario\n2) Crear promedio\n3) Salir")
        try:
            opc = int(input(":"))
            if opc == 1:
                if Max_usuarios > len(usuarios):
                    Ingreso_datos(usuarios)
                else:
                    print()
                    print("Limite de usuarios alcanzado\n(MAX. usuarios : 3)")


            elif opc == 2:
                calculo_promedio()

            elif opc == 3:
                print()
                print("Cerrando Menú")
                print("...")
                time.sleep(1)
                break
        except ValueError:
            print("Ingrese una opcion valida")

Menu()
