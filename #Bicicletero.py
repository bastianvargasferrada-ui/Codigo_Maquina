#Bicicletero

Dias = 0
Estudiante_Confirm = ""
total_Bici = 15000
descuento = 0
total_candado = 9000


print("--Encuesta para descuento--")
Estudiante_Confirm = input("Es usted estudiante(S/N): ")
Dias = int(input("Ingrese la cantidad de días de uso que lleva: "))
if Estudiante_Confirm == "S":
    if 20 < Dias:
        descuento = (15000*25)//100
        total_Bici -= descuento
        print("¡¡Felicidades!!")
        print("Ha obtenido un descuento del 25%")
        print("Queda con un total de:\nBicicletero","=", total_Bici)
    elif Dias >= 10 and Dias < 20:
        descuento = (15000*15)//100
        total_Bici -= descuento
        print("¡¡Felicidades!!")
        print("Ha obtenido un descuento del 15%")
        print("Queda con un total de:\nBicicletero","=", total_Bici)
elif Estudiante_Confirm == "N":
    if 20 < Dias:
        descuento = (15000*15)//100
        total_Bici -= descuento
        print("¡¡Felicidades!!")
        print("Ha obtenido un descuento del 15%")
        print("Queda con un total de:\nBicicletero","=", total_Bici)
    elif Dias >= 10 and Dias < 20:
        descuento = (15000*8)//100
        total_Bici -= descuento
        print("¡¡Felicidades!!")
        print("Ha obtenido un descuento del 8%")
        print("Queda con un total de:\nBicicletero","=", total_Bici)
    else:
        print("Lo sentimos, no cumple los requisitos para ningún descuento")
        print("Queda con uhn total de:\nBicicletero", "=", total_Bici)

if Estudiante_Confirm == "S":
    if Dias >= 15:
        descuento = (9000*15)//100
        total_candado -= descuento
        print("Adicionalmente se le ha aplicado un descuento del 15%",
        "por el candado")
        print("Queda con un total de:\nCandado","=", total_Bici)
    else:
        descuento = (9000*10)//100
        total_candado -= descuento
        print("Adicionalmente se le ha aplicado un descuento del 10%",
        "por el candado")
        print("Queda con un total de:\nCandado","=", total_candado)
elif Estudiante_Confirm == "N":
    print("Candado: ", total_candado)


