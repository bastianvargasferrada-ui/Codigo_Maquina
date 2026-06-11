#Entrega de libros

Estudiantes = {

}

def Ingreso_estudiante():
    print()
    print("|== Ingreso de estudiantes ==|")
    print("Ingrese el nombre del estudiante")
    NOMBRE = input(":").upper()
    print("Ingrese la cantidad de libros leídos")
    try:
        while True:
            LEIDOS = int(input(":"))
            if LEIDOS < 0:
                print("Cantidad de libros invalida")
                print("Intente con otro valor")
            else:
                Estudiantes[NOMBRE] = {
                    "Leídos": LEIDOS
                }
                return Estudiantes
    except ValueError:
        print("Porfavor, ingrese valores validos ")


def promedio_libros():
    suma_libros = 0
    promedio = 0
    if len(Estudiantes) == 0:
        print("No es posible calcular el promedio")
        return
    else:
        for estudiante in Estudiantes.values():
            suma_libros += estudiante["Leídos"]
        promedio = suma_libros//len(Estudiantes)
        print("| Promedio |")
        print("El promedio es de ", promedio)

def Más_libros():
    print()
    mejor_estudiante = max



def Menu():
    opc = 0
    Usuarios_max = 4
    while True:
        print()
        print("|== Menú principal ==|")
        print("1) Ingresar estudiante\n2) Calcular promedio de libros leídos\n3) Mostrar estudiante con mayor libros leídos")
        print("4)Salir")
        try:
            opc = int(input(":"))
            match opc:
                case 1:
                    print(len(Estudiantes))
                    if len(Estudiantes) <  Usuarios_max:
                        Ingreso_estudiante()
                    else:
                        print("Ha alcanzado la cantidad maxima de estudiantes registrados")
                case 2:
                    promedio_libros()
                case 3:
                    print("Opción no desarrollada")
                case 4:
                    print("Cerrando Menú")
                    print("Hasta pronto")
                    break
                case _:
                    print("No se ha encontrado dicha opción")
        except ValueError:
            print("Solo ingrese numeros")

Menu()