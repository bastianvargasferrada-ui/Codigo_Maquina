#INTENTO 1 PRIMER ITEM 1

#valores generales
bicicletero = 15000
Candado = 9000
#Variables principales
Estudiante_CF = "" #CF = Confirmacion
Dias = 0
#Variables para descuento
desct_Bici = 0
desct_cand = 0
Desct_AD = 0



print("¿Es estudiante?: (S/N)")
Estudiante_CF = input()
print("Ingrese días de uso de este mes: ")
Dias =int(input())

def Mensaje():
    print("Felicidades, se le ha aplicado un descuento del ", desct_Bici)



if Estudiante_CF == "S":
    if Dias >= 20:
        desct_Bici = (bicicletero * 25)//100
        bicicletero -= desct_Bici
        Mensaje()
    elif Dias < 20 and Dias >= 10:
        desct_Bici = (bicicletero * 15)//100
        bicicletero -= desct_Bici
        Mensaje()
    elif Dias < 10:
        print("No tiene la cantidad de dias suficientes para un descuento")
        bicicletero
elif Estudiante_CF == "N":
    if Dias >= 20:
        desct_Bici = (bicicletero * 15)//100
        bicicletero -= desct_Bici
        Mensaje()
    elif Dias < 20 and Dias >= 10:
        desct_Bici = (bicicletero * 8)//100
        bicicletero -= desct_Bici
        Mensaje()
    elif Dias < 10:
        print("No tiene la cantidad de dias suficientes para un descuento")
        print("Su biciletero queda con un valor de: ", bicicletero)

if Estudiante_CF == "S":
    desct_cand = (Candado * 10)//100
    Candado -= desct_cand
    print("Felicidades, se le ha aplicado un descuento del ", desct_cand)
    if Dias >= 15:
        Desct_AD = (Candado * 5)//100
        Candado -= Desct_AD
        print("Adicionalmente se la aplico también un descuento del", Desct_AD, "por la cantidad de días")

print("")
print("Quedando con un valor final del:\nBicicletero", "x", bicicletero, "\nCandado", "x", Candado)






