#Diccionario y listas
#Maquina de bebidas

Total = 0

def Menú():
    Opc = 9999
    Lista_Bebidas = []
    while Opc != 0:
        print("--Menú--")
        print("1)Coca cola\n2)Fanta\n3)Kem\n4)Pepsi\n5)Limonsoda\n6)becker\n0)Terminar")
        print("Seleccione un producto")
        Opc =int(input(":"))
        match Opc:
            case 1:
                Lista_Bebidas.append("Coca cola")
            case 2:
                Lista_Bebidas.append("Fanta")
            case 3:
                Lista_Bebidas.append("Kem")
            case 4:
                Lista_Bebidas.append("Pepsi")
            case 5:
                Lista_Bebidas.append("Limonsoda")
            case 6:
                Lista_Bebidas.append("Becker")
            case 0:
                print("Pedido finalizado ")

    return Lista_Bebidas

def main():
    Opc = 9999
    Lista_Bebidas_Main = []
    while Opc != 0:
        print("1)Realizar pedido\n2)Ver lista\n3)Pagar\n4)Cancelar\n0)Salir")
        print("Seleccione opcion")
        Opc = int(input(":"))
        match Opc:
            case 1:
                Lista_Bebidas_Main = Menú()
            case 2:
                print(Lista_Bebidas_Main)
    
main()
            




