#Clasificación de ejercutivos

Bucle1 = True
ejercutivo_num = 0
Ejecutivo_nom = ""
contador_gerentes = 0
contador_analista = 0

def Ingreso_nom():
    global ejercutivo_num    #Usamos las 2 variables globales para no tener que declararlas de forma local
    global Ejecutivo_nom
    global Bucle2
    global contador_analista
    global contador_gerentes
    vueltas = 0
    print()
    while vueltas < ejercutivo_num:
        Nombre_invalido = True

        while Nombre_invalido:
            print("Ingrese un nombre para el ejecutivo: ")
            Ejecutivo_nom = input(":")
            if Vali_espacios(Ejecutivo_nom) or Vali_largo(Ejecutivo_nom):
                print("Nombre invalido")
            else:
                print("Nombre valido")
                Años_exp()
                vueltas += 1
                Nombre_invalido = False
    print(f"""¡El banco cuenta con {contador_gerentes} Gerentes Ejecutivos 
y {contador_analista} Analistas Financieros! ¡Operaciones auto-rizadas!""")
            
            
    
        
        
def Vali_largo(Ejecutivo_nom):
    MIN_CARACT = 6     #numero minimo de caracteres
    Largo_nom = len(Ejecutivo_nom)
    if MIN_CARACT > Largo_nom:
        print(" El nombre debe tener al menos 6 caracteres")
        return True
    else:
        return False

def Vali_espacios(Ejecutivo_nom):
    contador_espacios = 0
    MAX_espacios = 0
    print()
    for letra in (Ejecutivo_nom):
        if letra.isspace():
            contador_espacios += 1
    if contador_espacios > MAX_espacios:
        print("No puede contener espacios")
        print(contador_espacios)
        return True
    else:
        return False

def Años_exp():
    global contador_analista
    global contador_gerentes
    print()
    Años_invalido = True
    while Años_invalido:
        try:
            print("Ingrese los años de experiencia:")
            años_exp = int(input(":"))
            if años_exp < 0:
                print("¡Error financiero! Ingresa un número entero positivo para la antigüedad.")
            else:
                if años_exp > 3:
                    contador_gerentes += 1
                    Años_invalido = False
                else:
                    contador_analista += 1
                    Años_invalido = False
        except ValueError:
            print("¡Error financiero! Ingresa un número entero positivo para la antigüedad.")



while Bucle1:
    print("¿ Cuantos ejercutivos desea ingresar ?")      #Iniciamos el bucle solicitando el numero de ejecutivos
    try:
        ejercutivo_num = int(input(":"))
        if ejercutivo_num < 0:           # validamos que sea un valor positivo
            print(" ¡Transacción inválida! Ingresa un entero positivo para continuar ")
        else:
            Bucle1 = False   #si todo esta correcto, se cancela el bucle y se ejecuta la funcion siguiente
            Ingreso_nom()
    except ValueError:  #validamos que sea un numero
        print(" ¡Transacción inválida! Ingresa un entero positivo para continuar ") 
    
