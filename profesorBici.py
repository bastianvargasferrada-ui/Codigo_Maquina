bicicletero = 15000
candado = 9000
cantDias = 0
alumnoRegular = 0
totalBicicletero = 0
totalCandado = 0
 
 
print("Ingrese cantidad de días:")
cantDias = int(input())
print("Ingrese si es estudiante regular 1)Si 2)No")
alumnoRegular = int(input())
 
 
if cantDias >= 20:
    if alumnoRegular == 1:
        totalBicicletero = bicicletero * 0.75
        
    else:
        totalBicicletero = bicicletero * 0.85
elif cantDias >= 10 and cantDias < 20:
    if alumnoRegular == 1:
        totalBicicletero = bicicletero * 0.85
    else:
        totalBicicletero = bicicletero * 0.92
else:
    totalBicicletero = bicicletero
 
 
if alumnoRegular == 1:
    if cantDias >= 15:
        totalCandado = candado * 0.85
    else:
        totalCandado = candado * 0.9
else:
    totalCandado = candado
 
 
print("El valor del bicicletero es: ", int(totalBicicletero))
print("El valor del candado es:", int(totalCandado))