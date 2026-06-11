#Claificación medicos 2

bucle1 = True
med_num = 0
contador_especialista = 0
contador_residente = 0

def Años_exp():
    global contador_especialista
    global contador_residente
    años_invalido = True
    try:
        while años_invalido:
            print()
            print("Ingrese los años de experiencia del médico")
            años_exp = int(input(":"))
            if años_exp < 0:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
            else:
                if años_exp > 5:
                    print()
                    contador_especialista += 1
                    años_invalido = False
                elif años_exp <= 5:
                    print()
                    contador_residente += 1
                    años_invalido = False
    except ValueError:
        print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")



def validar_largo(nom_med):
    Largo = len(nom_med)
    MIN_LARGO = 6
    if Largo < MIN_LARGO:
        print("El nombre es demasiado corto")
        return True
    else:
        return False


def validar_espacios(nom_med):
    contador_espacios = 0
    MAX_ESPACIOS = 0
    for letra in nom_med:
        if letra.isspace():
            contador_espacios += 1
    if contador_espacios > MAX_ESPACIOS:
        print("No debe contener espacios")
        return True
    else:
        return False



def nombres_medicos(): 
    vueltas = 0
    while vueltas < med_num:
        nombre_invalido = True
        while nombre_invalido:
            print("Ingrese el nombre del médico: ")
            nom_med = input(":")
            if validar_espacios(nom_med) or validar_largo(nom_med):
                print("Nombre invalido")
            else:
                print("Nombre valido")
                vueltas += 1
                nombre_invalido = False
                Años_exp()
    print(f"""¡El hospital cuenta con {contador_especialista} Especialistas Senior
 y {contador_residente} Residentes Junior! ¡Sistema listo para operar!""")
    


while bucle1:
    try:
        print()
        print("Ingrese la cantidad de medicos que desea registrar")
        med_num = int(input(":"))
        if med_num < 0:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
        else:
            print()
            bucle1 = False
            nombres_medicos()
    except ValueError:
        print()
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")


