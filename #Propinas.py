#Propinas
Monto_Cuenta = 0
Propina = 0
Propina_Totales = 0
Comando = ""

print("PROPINAS")
print()
while True:
    print("Menú principal")
    Monto_Cuenta = int(input("Ingrese la cuenta de la mesa: "))
    Propina = (Monto_Cuenta*10)//100
    print("--Visualización de propina y su acumlado--")
    print("Su propina es", Propina)
    Propina_Totales+= Propina
    print("Su propina total acumulada es", Propina_Totales)
    Comando = input("Si desea continuar, presione enter\nde lo contrario, escriba 'Cerrar caja': ")
    print()
    if "Cerrar caja" == Comando:
        print("Cerrando caja")
        print("...")
        print("Su total de propinas acumuladas es: ", Propina_Totales)
        break