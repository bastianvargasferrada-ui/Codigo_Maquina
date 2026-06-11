#Menú Ingreso de usuarios
import time

usuarios = {

}



def Ingreso_de_datos(): #Función para crear un usuario mediante el ingreso de sus datos
    print("Ingresa un RUT")  #pedimos RUT, usamos input, por si su RUT termina con k
    RUT = input(":").upper()
    print("Ingresa el nombre")
    NOMBRE = input(":").upper()
    print("Ingresa la edad")      #Usamos try para controlar el error de value error en caso de que el usuario
    try:                          #ingrese una letra en vez de un numero
        EDAD = int(input(":"))
    except ValueError:
        print("Ingrese solo numeros")
    
    usuarios[RUT] = { "Nombre": NOMBRE,
                     "Edad": EDAD

    }

def Lista_Usuarios():
    print("Lista")
    for rut, datos in usuarios.items():
        print(f" Rut: {rut} | Datos: {datos}")

def Buscar_usuario():
    print()
    print("Ingrese el RUT del usuario")
    Buscar_Rut = input(":")
    if Buscar_Rut in usuarios:
        print(usuarios[Buscar_Rut])
    else:
        print("El usuario no se encuentra en la lista")



def Menu():
    opc = 99999
    while True:
        print
        print("|== Menú ==|")
        print("Seleccione una opción: ")
        print("1) Ingresar datos de usuario\n2) Ver lista de usuarios\n3) Buscar usuario\n0) Salir ")
        try:
            opc = int(input(":"))
        except ValueError:
            print("Ingrese una opción númerica")
        
        match opc:  
            case 1:
                Ingreso_de_datos()
            case 2:
                Lista_Usuarios()
            case 3:
                Buscar_usuario()

            case 0:
                print()
                print("Cerrando menú")
                time.sleep(1)
            case _:
                print("No se ha encontrado ninguna opción co ese valor")


Menu()
