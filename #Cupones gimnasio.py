#Cupones gimnasio
import time

CUPONES = 75
TOTAL_RESERVAS = 0

print("¡Bienvenido al sistema de gestión de cupos del Gimnasio Titan!")

def Reservas():
    global CUPONES
    global TOTAL_RESERVAS
    Reserva_num = 0
    print()
    print("***RESERVA***")
    print("Ingrese el numero de cupos que desea reservar")
    try:
        Reserva_num = int(input(":"))
        if Reserva_num < 0:
            print("Opción invalida")
        elif Reserva_num > CUPONES:
            print("La cantidad seleccionada excede la cantidad de cupones disponibles")
        else:
            CUPONES -= Reserva_num
            
            print("Felicidades, la reserva se ha realizado con exito")
            print(f"Número de cupones reservados: {Reserva_num}")
            TOTAL_RESERVAS += 1
    except ValueError:
        print("Ingrese un numero valido")

def Cancerlar_reservas():
    global CUPONES
    global TOTAL_RESERVAS
    TOTAL_CUPONES = CUPONES
    print()
    print("***CANCELAR RESERVAS***")
    print("Ingrese la cantidad de cupones que desea cancelar")
    try:
        Cancel_num = int(input(":"))
        if Cancel_num < 0:
            print("Ingrese numeros positivos")
        else:
            TOTAL_CUPONES += Cancel_num
            if TOTAL_CUPONES > 75:
                print("Monto excesivo de cupones a cancelar")
                return
            else:
                CUPONES = TOTAL_CUPONES
                print("Felicidades, cancelación realizada con éxito")
                print(f"Cantidad de cupones cancelados: {Cancel_num}")
                TOTAL_RESERVAS -= 1
                if TOTAL_RESERVAS < 0:
                    TOTAL_RESERVAS = 0
                else:
                    TOTAL_RESERVAS
    except ValueError:
        print("Ingrese un numero valido")



def Menu_principal(): 
    opc = 0
    while True:
        print()
        print("***MENU PRINCIPAL***")
        print("1.-Cupos disponibles\n2.-Realizar reserva\n3.-Cancelar reserva\n4.-Historial de reservas\n5.-Salir")
        try:
            opc = int(input(":"))
            match opc:
                case 1:
                    print()
                    print("El numero de cupones disponibles son: ", CUPONES)
                case 2:
                    Reservas()
                case 3:
                    Cancerlar_reservas()
                case 4:
                    print()
                    print("***HISTORIAL DE RESERVAS***")
                    print(f"Las reservas realizadas en esta sesión son: {TOTAL_RESERVAS}")
                case 5:
                    print()
                    print("Cerrando Menú")
                    print("Gracias por utilizar nuestro software, hasta la próxima!")
                    time.sleep(1)
                    break
                case _:
                    print("No se ha encontrado esa opción")


        except ValueError:
            print(" Ingresa una opcion valida")

Menu_principal()
