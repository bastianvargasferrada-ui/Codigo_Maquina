#Cajero automatico 1.5

#Listas del Menú
opc_list =[1, 2, 3, 4, 0]
#Listas generales del cajero
cant_billetes = [5, 4, 6, 7, 9]
Billetes = [20000, 10000, 5000, 2000, 1000]
#Aquí van las listas utilizadas para la opción de giros
opc_giro = [1, 2, 3, 4, 5, 6]
cant_giro = [5000, 10000, 20000, 50000, 80000, 100000]
Monto_Restante = 0
#Datos del usuario
pin = 123
Nuevo_pin = 0
intento = 0
Saldo = 90000




def Menú(opciones):
  print("---Menú---\nIngrese una opción\n1.-Consultar saldo\n2.-Depositar\n3.-Girar\n4.-Cambiar pin\n0.-Salir")

while intento != pin:
 intento = int(input("Ingrese su pin: "))
 if intento != pin:
     print("pin incorrecto, pruebe de nuevo")
    
while opc_list != 0:
    Menú(opc_list)
    opc_list = int(input(":"))
    if opc_list > 4 or opc_list < 0:
        print("Opción invalida, ingrese de nuevo una opción: ")
        Menú(opc_list)
        opc_list = int(input(":"))
    else:
        print("procesando...")
        match opc_list:
            case 1:
                print("--Saldo--")
                print("Su saldo es: ", Saldo)
            case 2:
                print("--Deposito--")
                Deposito = int(input("Ingrese el deposito: "))
            case 3:
                print("--giro--")
                print("Ingrese la cantidad que desea girar: ")
                print("1.- 5.000\n2.- 10.000\n3.- 20.000\n4.- 50.000\n5.- 80.0000\n6.- 100.0000")   #cant_billetes = [5, 4, 6, 7, 9]
                opc_giro = int(input(":"))                                                          
                Monto = cant_giro[opc_giro - 1]
                if Monto < Saldo:
                    Monto_Restante = Monto
                    Billetes_usados = [0, 0, 0, 0, 0]

                    print("su monto a girar es:", Monto)
                    print("entrtegando billetes: ")       ##Billetes = [20000, 10000, 5000, 2000, 1000]
                    for i in range(len(Billetes)):
                        Billete = Billetes[i]
                        B_Disponibles = cant_billetes[i]
                        
                        B_Necesario = Monto_Restante//Billete
                        Billetes_a_usar = min(B_Disponibles, B_Necesario)

                        Billetes_usados[i] = Billetes_a_usar
                        Monto_Restante -= Billetes_a_usar * Billete

                    if Monto_Restante == 0:
                        print("Retiro exitoso")
                        for i in range(len(Billetes)):
                            if Billetes_usados[i] > 0:
                                print("usted lleva\n", {Billetes_usados[i]}, "x", {Billetes[i]})
                                cant_billetes[i] -= Billetes_usados[i]
                        Saldo -= Monto
                    else:
                            print("No se puede entregar el monto solicitado con la cantidad actual de billetes")
                else:
                    print("Saldo insuficiente")
            


                    
                    
                  






            case 4:
                Nuevo_pin = int(input("Ingrese su nuevo pin: "))
                pin = Nuevo_pin
                print("Su nuevo pin es: ", pin)
            case 0:
                print("Hasta pronto!!")

            case _:
                print("Opción invalida")
    




