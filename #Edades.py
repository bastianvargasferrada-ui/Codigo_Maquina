#Edades

Edad = 1

while Edad != 0:
    Edad = int(input("Ingrese edad:"))
    if 0 < Edad < 18:
        print("Es menor de edad")
    elif 17 < Edad < 60:
        print("Es un adulto")
    elif 0 < Edad >= 60:
        if Edad > 100:
            print("Edad invalida")
        else:
            print("Es adulto mayor")
    else:
        print("Edad invalida")


