#Biblioteca


correo = ""

def Validar_Largo(correo):       #Con esta funcion validamos el largo del correo y ver si cumple o no las condiciones
    Largo_Max = 35  #Definimos el largo maximo
    Largo_Min = 15  #Definimos el Largo minimo
    Largo_correo = len(correo) #Y asignamos el largo del correo por puro orden
    if Largo_correo > Largo_Max:      #Hacemos la compración por cada variable
        print("Correo muy largo")
        return True                   #Si es muy largo o corto, notificará que el correo no cumple con esa condición,
    elif Largo_correo < Largo_Min:    # y retornará True
        print("Correo muy corto")
        return True
    else:
        return False               #De lo contrário retornrá false, y cumplirá una de las condiciones

def Existencia_arroba(correo): #Con esta función validamos si el correo contiene uno o más arrobas
    contador_arroba = 0 #Un contador para controlar la cantidad de @
    for caracter in correo: #Bucle for para verificar cada caracter del correo
        if caracter == "@":
            contador_arroba += 1 #Si detecta un arroba, se suma al contador
    if contador_arroba == 0: #Si el contador final es igual a cero, no cumplirá la condición
        print("No contiene arroba")
        return True #Se le notificará y retornará True
    elif contador_arroba > 1: #Si el contador es mayor a 1, no cumplirá la condición
        print("No puede contener 2 arrobas") 
        return True
    else:
        return False #Si ha cumplido las condiciones, cumplirá esta condición
    
def Validar_dominio(correo): #Con esta función validamos el dominio del correo
    dominio = correo[-14 : ]  #Asignamos como dominio la parte del correo [-14 : ], no ponemos para que vea hasta el final
    if dominio != "@biblioteca.cl":  #Y aquí es una simple comparación, lo mismo que hemos hecho arriba
        print("El dominio debe ser: '@biblioteca.cl'")
        return True
    else:
        return False

def Antes_Arroba_C(correo):
    pre_arroba = correo[0 : -14]
    Caracteres_min = 6
    if len(pre_arroba) < Caracteres_min:
        print("Caracteres minimos antes del arroba : 6")
        return True
                
    else:
        return False

def Validación_Primer_C(correo):# Valida el primer caracter del correo
    Primer_caracter= correo[0]
    Primer_no_permitido = ". _"
    if Primer_caracter.isdigit():
        print("El primer caracter del correo debe ser una letra")
        return True
    elif Primer_caracter in Primer_no_permitido:
        print("No puede empezar ni terminar con '.' o '_'")
        return True
    
    else:
        return False

def Antes_Arroba_LyP(correo): #Funcion para validar si hay letras y caracteres prohibidos
    pre_arroba = correo[0 : -14]
    contador_num = 0
    contador_pro = 0
    prohibido_min = 0
    num_min = 1
    Lista_prohibidos = ", ; : ¿ ? ¡ ! ' - + * / = % < > $ @ & © ® ™ | ^ ~ [ ] { } *"
    for caracter in pre_arroba:
        if caracter.isdigit():
            contador_num += 1
        if caracter in Lista_prohibidos:
            contador_pro += 1
    if contador_num < num_min:
        print("Debe haber al menos un numero antes del correo")
        return True
    elif contador_pro > prohibido_min:
        print("Solo pueden haber letras, números, '.' y '_' antes del arroba")
        return True
    else:
        return False

def Validador_espacios(correo):
    contador_espacio = 0
    for caracter in correo:
        if caracter.isspace():
            contador_espacio += 1
    if contador_espacio > 0:
        print("No puede contener espacios")
        return True
    else:
        return False

def Validador_puntos_seguidos(correo):
    if ".." in correo:
        print("No se permiten puntos seguidos")
        return True
    else:
        False

def Menu_principal():
    while True:
        print()
        print("Ingrese su correo")
        correo = input(":")
        Validaciones_correo = [
            Validar_Largo(correo),
            Existencia_arroba(correo),
            Validar_dominio(correo),
            Antes_Arroba_C(correo),
            Validación_Primer_C(correo),
            Antes_Arroba_LyP(correo),
            Validador_espacios(correo),
            Validador_puntos_seguidos(correo)
        ]
        if any(Validaciones_correo):
            print("Correo invalido")
            print("Pruebe con otro")
        else:
            print("Correo valido")
            break

Menu_principal()
    