#Gastos

Gasto = 0
Gasto_Total = 0
promedio = 0
for i in range(7):
    print("dia", i + 1)
    Gasto = int(input("Ingrese el valor del gasto: "))
    Gasto_Total += Gasto
print("Su gasto total es", Gasto_Total)
promedio = Gasto_Total//7
print("Y en promedio gasta", promedio, "por día")
if promedio > 50000:
    print("Su gasto es elevado")
else:
    print("Gasto adecuado")

    