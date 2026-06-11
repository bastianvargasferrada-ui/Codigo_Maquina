#Cajero automatico 1.0
opcion = 1
#Contraseña usuario
pin = 123
Nuevo_pin = 0
intento = 0
Saldo = 60000
intento = 0
contador_intentos = 0
#Opción de deposito
Deposito = 0
Nuevo_Saldo = 0
#Contador de billetes
contadorMil = 10
contadorDosMil = 10
contadorCincoMil = 10
contadorDiezMil = 10
contadorVeinteMil = 10
#Tipos de giros
Retiro_Veinte = 0
Retiro_Diez = 0
Retiro_Cinco = 0
Retiro_Dos = 0
Retiro_Mil = 0
#Total cajero
totalCajero = contadorMil*1000 + contadorDosMil * 2000 + contadorCincoMil * 5000 + contadorDiezMil * 10000 + contadorVeinteMil * 20000


while intento != pin:
      intento =int(input("Ingrese su pin: "))
      if intento == pin:
            print("Pin correcto")
      else:
           print("contraseña incorrecta")
           contador_intentos += 1
           if contador_intentos > 3:
                print("Tarjeta bloqueada")
                break
            

print()



while opcion !=0:
     print("--Menú--")
     print("1. Consultar saldo")
     print("2. Depositar")
     print("3. Girar")
     print("4. Cambiar pin")
     print("0. Salir")
     print("Seleccione una opción")
     opcion = int(input(":"))

     print()


     match opcion:
         case 1:
             print("Saldo")
             print("Su saldo es:", Saldo)
         case 2:
               print("--Depositar--")
               Deposito = int(input("Ingrese la cantidad a ingresar: "))
               Saldo += Deposito
               Nuevo_Saldo = Saldo

               print("Su nuevo saldo es: ", Saldo)

         case 3:
               print("--Girar--")
               giro = int(input("Ingrese la cantidad a retirar: "))
               if giro > Saldo:
                print("Saldo insuficiente")
               else:
                Restante = giro

                Retiro_Veinte = Restante//20000
                Restante -= Retiro_Veinte*20000

                Retiro_Diez = Restante//10000
                Restante -= Retiro_Diez*10000

                Retiro_Cinco = Restante//5000
                Restante -= Retiro_Cinco*5000

                Retiro_Dos = Restante//2000
                Restante -= Retiro_Dos*2000

                Retiro_Mil = Restante//1000
                Restante -= Retiro_Mil*1000

                if Restante == 0:
                    print("Retiro exitoso")
                    print("Usted lleva ", Retiro_Veinte, " billetes de 20.000")
                    print("Usted lleva ", Retiro_Diez, " billetes de 10.000")
                    print("Usted lleva ", Retiro_Cinco, " billetes de 5.000")
                    print("Usted lleva ", Retiro_Dos, " billetes de 2.000")
                    print("Usted lleva ", Retiro_Mil, " billetes de 1.000")
    
                    contadorMil -= Retiro_Mil
                    contadorDosMil -= Retiro_Dos
                    contadorCincoMil -= Retiro_Cinco
                    contadorDiezMil -= Retiro_Diez
                    contadorVeinteMil -= Retiro_Veinte
    
                    Saldo-= giro
                else:
                   print("Cantidad de billetes insuficientes en el cajero")

               
         case 4:
               print("Cambio de pin")
               

               
               Nuevo_pin = int(input("Ingrese su nuevo pin: "))
               Nuevo_pin = pin
               Confirmación_Pin = int(input("Vuelva a ingresar su nuevo pin: "))
               if Nuevo_pin == Confirmación_Pin:
                    print("Cambio de pin exitoso")
                    print("Su nuevo pin es", pin)
                    print()

         case 0: 
               print("¡Adios!")
         case _:
               print("Opción incorrecta")

