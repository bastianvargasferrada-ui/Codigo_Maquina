#Maquina expendedora
#Pedir un monto de dinero
#Entregar el vuelto usando monedas disponibles
#Respetar la cantidad de monedas que tiene la máquina

Monedas_list = [500, 100, 50, 10]
Cant_Monedas = [5, 10, 8, 20]

opc = 1
Monto_Restante = 0




while opc != 0:
    print("--Menú--")
    Monto = int(input("Ingrese un monto: "))
    print("entregando vuelto...")

    print()
    Monto_Restante = Monto

    Moneda_Usadas = []

    for i in range(len(Monedas_list)):
        Moneda = Monedas_list[i]
        Monedas_Disp = Cant_Monedas [i]

        Necesito = Monto_Restante // Moneda
        Moneda_a_usar = min(Necesito, Monedas_Disp)
        



