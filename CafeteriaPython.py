def menu():
    #VARIABLES LOCAL
    opcion = 1
    while opcion != 0:
        print("BIENVENIDO A CAFETERÍA")
        print("==Lista de Productos==")
        print("1) Comprar Bebestibles")
        print("2) Comprar Comestibles")
        print("3) Pagar")
        print("0) Salir")
        print("Seleccione una opción")
        opcion = int(input())
        return opcion
    
def compraBebestibles():
    opcion = 1
    bebestible = {}
    listaBebestible = []
    while opcion != 0:
        print("==Compra de Bebestibles==")
        print("1) CAFE $2.000")
        print("2) BEBIDA $1.000")
        print("3) AGUA $1.500")
        print("0) VOLVER")
        print("Seleccione bebestible")
        opcion = int(input())

        match opcion:
            case 1:
                bebestible = {
                    "PRODUCTO" : "CAFE",
                    "VALOR" : 2000
                }
            case 2:
                bebestible = {
                    "PRODUCTO" : "BEBIDA",
                    "VALOR" : 1000
                }
            case 3:
                bebestible = {
                    "PRODUCTO" : "AGUA",
                    "VALOR" : 1500
                }
            case 0:
                return listaBebestible
            case _:
                print("Seleccione un Bebestible")
        listaBebestible.append(bebestible)


def compraComestibles():
    print("==Compra Comestibles==")

def pagar():
    print("==Pagar==")


#PROGRAMA PRINCIPAL
#VARIABLES GLOBALES
opcionGlobal = 0
opcionGlobal = menu()
listaBebestibleGlobal = []
match opcionGlobal:
    case 1:
        listaBebestibleGlobal = compraBebestibles()
        print("Usted lleva: ")
        for bebestible in listaBebestibleGlobal:
            print(bebestible)
    case 2:
        compraComestibles()
    case 3:
        pagar()
    case 0:
        print("==¡Muchas gracias!==")
    case _:
        print("Opción Inválida. Seleccione una opción correcta")
        opcionGlobal = menu()