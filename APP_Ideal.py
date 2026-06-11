suma = 0

print("Registro de actividades diarias")

while True:
    print("----- Menú -----")
    print("1) Registrar actividades")
    print("2) Mostrar análisis de tiempo")
    print("3) Salir")
    
    opc = int(input("Seleccione una opción: "))
    
    if opc == 1:
        num_act = int(input("¿Cuántas actividades desea registrar?: "))
        
        if num_act >= 3:
            for i in range(num_act):
                nom_act = input("Ingrese nombre de la actividad: ")
                time_act = int(input("¿Cuánto tiempo toma dicha actividad?: "))
                
                suma += time_act  # equivalente a suma = suma + time_act
        else:
            print("Debe ingresar al menos 3 actividades")
    
    elif opc == 2:
        print("El tiempo total de todas las actividades es:", suma)
        
        if suma > 180:
            print("Su tiempo es excesivo")
        else:
            print("Su tiempo diario es adecuado")
    
    elif opc == 3:
        print("Fin del registro")
        break
    
    else:
        print("Opción inválida")