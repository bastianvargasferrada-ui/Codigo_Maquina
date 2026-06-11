#Cajero automatico

opc_list =[1, 2, 3]
pin = "0592"
intento = ""
Saldo = 5000

def Menú(opciones):
  print("---Menú---\nIngrese una opción\n1.-Ver saldo\n2.-Depositar dinero\n3.-Retirar dinero")




while intento != pin:
 intento = input("Ingrese su pin: ")
 if intento != pin:
     print("pin incorrecto, pruebe de nuevo")
    



Menú(opc_list)
opc_list = int(input(":"))
while opc_list > 3:
  print("Opción invalida")
  Menú(opc_list)
  opc_list = int(input(":"))
  






if opc_list<= 3:
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
            Ingreso = int(input("Ingrese la cantidad que desea girar: "))
    




