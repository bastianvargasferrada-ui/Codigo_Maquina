#Gestor de libros disponibles

Libros_disponibles = 120
Maximo_libros = 120
Contador_historial = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")


def Realizar_prestamo():
    global Libros_disponibles
    global Contador_historial
    libros_a_prestar = 0
    prestar = True
    while prestar:
        print()
        print("***PRÉSTAMO***")
        print("¡Buenos días!")
        try:
            print("Ingrese la cantidad de libros que desea pedir prestado: ")
            libros_a_prestar = int(input(":"))
            if libros_a_prestar < 0:
                print("Ingrese un número valido")
            elif libros_a_prestar > Libros_disponibles:
                print("La cantidad excede al numero de libros disponibles")
            else:
                print("¡Préstamo realizado con éxito!")
                print(f"Libros prestados: {libros_a_prestar}")
                Libros_disponibles -= libros_a_prestar
                Contador_historial += 1
                prestar = False
        except ValueError:
            print()
            print("Ingrese solo números")

def Devolver_prestamo():
    global Libros_disponibles
    global Maximo_libros
    global Contador_historial
    libros_a_devolver = 0
    prestar = True
    try:
        while prestar:
            print()
            print("***DEVOLVER PRÉSTAMO***")
            print("INgrese la cantidad de libros que desea devolver: ")
            libros_a_devolver = int(input(":"))
            Suma_temporal = libros_a_devolver + Libros_disponibles
            if libros_a_devolver < 0:
                print()
                print("Ingrese numeros validos")
            elif libros_a_devolver > Maximo_libros:
                print()
                print("la cantidad excede el limite maximo de capacidad de la biblioteca")
            elif Suma_temporal > Maximo_libros:
                print("Cantidad no valida, no coincide con el maximo de libros")
            else:
                print()
                print("Devolución lograda con éxito")
                print(f"Libros devueltos: {libros_a_devolver}")
                Libros_disponibles += libros_a_devolver
                Contador_historial -= 1
                if Contador_historial < 0:
                    Contador_historial = 0
                prestar = False
    except ValueError:
        print()
        print("¡ERROR! Ingrese solo numeros")

def Historial_prestamos():
    global Contador_historial
    print()
    print("***   HISTORIAL PRÉSTAMOS/DEVOLUCIONES    ***")
    print(f"Prestamos activos: {Contador_historial}")


def Menú():
    global Libros_disponibles
    opc = 0
    Menu_P = True
    while Menu_P:
        try:
            print("===MENÚ PRINCIPAL===")
            print("1.	Libros disponibles")
            print("2.	Realizar préstamo")
            print("3.	Devolver préstamo")
            print("4.	Historial de préstamos")
            print("5.	Salir")
            
            print("Ingrese una opción: ")
            opc = int(input(":"))
            if opc < 0:
                print("Opción invalida")
            else:
                match opc:
                    case 1:
                        print()
                        print("*** LIBROS DISPONIBLES ***")
                        print(Libros_disponibles)
                    case 2:
                        Realizar_prestamo()
                    case 3:
                        Devolver_prestamo()
                    case 4:
                        Historial_prestamos()
                    case 5:
                        print()
                        print("Gracias por utilizar nuestro software, hasta la próxima.")


        except ValueError:
            print()
            print("¡ERROR! Ingrese un valor valido")

Menú()