#Verificador de contraseñas

contraseña = "pepito01"
intento = ""
contador_intentos = 0

while intento != contraseña:
    intento = input("Ingrese su contraseña: ")
    if intento != contraseña:
        print("Contraseña incorrecta")
        contador_intentos += 1
        if contador_intentos == 3:
            print("Cantidad de intentos excedidos\nBloqueando cuenta...")
            break
    else:
        print("Contraseña correcta")
