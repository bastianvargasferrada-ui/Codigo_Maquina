#Medicamentos

Medicamentos_mensual = 60000
med_descuentos = 0
despacho_domicilio =8000
desp_descuento = 0
desp_descuento_adc = 0
Edad = 0 
tramo = ""






Edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ")
if Edad <= 30:
    if tramo == "A" or tramo == "B":
        med_descuentos = (Medicamentos_mensual*18)//100
        Medicamentos_mensual -= med_descuentos
        print(Medicamentos_mensual)
    elif tramo == "C" or tramo == "D":
        med_descuentos = (Medicamentos_mensual*12)//100
        Medicamentos_mensual -= med_descuentos
        print(Medicamentos_mensual)
elif Edad >= 31 and Edad <= 60:
    if tramo == "A" or tramo == "B":
        med_descuentos = (Medicamentos_mensual*12)//100
        Medicamentos_mensual -= med_descuentos
        print(Medicamentos_mensual)
    elif tramo =="C" or tramo == "D":
        med_descuentos = (Medicamentos_mensual*8)//100
        Medicamentos_mensual -= 100
        print(Medicamentos_mensual)
else:
    print(Medicamentos_mensual)

if tramo == "A" or tramo =="B":
    desp_descuento = (despacho_domicilio*10)//100
    despacho_domicilio -= desp_descuento
    print("Ha obtenido un descuento en despacho por el tramo elegido")
    print("Despacho: ", despacho_domicilio)
    if Edad >= 55:
        desp_descuento_adc = (despacho_domicilio*8)//100
        despacho_domicilio -= desp_descuento_adc
        print("Ha obtenido un descuento adicional de", "$", desp_descuento_adc,"\nSu valor de despacho a sido actualizado")
        print("Descuento: ", despacho_domicilio)
elif tramo == "C" or tramo == "D":
    print("No se le ha aplicado ningún descuento a su despacho")
    print("Por lo que quede con un valor de")
    print("Despacho: ", despacho_domicilio)
        

    



