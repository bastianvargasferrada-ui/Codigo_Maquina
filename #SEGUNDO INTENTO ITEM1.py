#SEGUNDO INTENTO ITEM1


#Variables generales
Medicamentos = 60000
despacho = 8000
Tramo = ""
Edad = 0
#Variables descuento
descuent_med = 0   # Descuento para medicamentos  
descuent_despa = 0  # Descuentos para despacho
descuent_AD = 0  #Descuento adicional

def Mensaje_desct1():
    print("Felicidades, ha recibido un descuento del ", descuent_med, "\nEl valor de los medicamentos es: ", Medicamentos)

def Mensaje_desct2():
    print("Felicidades, ha recibido un descuento del ", descuent_despa, "\nEl valor de los medicamentos es: ",descuent_despa)




print("Ingrese el tramo elegido: (A, B, C o D)")
tramo = input(":")
print("Ingrese su edad: ")
edad = int(input(":"))

if tramo == "A" or tramo =="B":
    if edad <= 30:
        descuent_med = (Medicamentos * 18)//100
        Medicamentos -= descuent_med
        Mensaje_desct1()
    elif edad >= 31 and edad <= 60:
        descuent_med = (Medicamentos * 12)//100
        Medicamentos -= descuent_med
        Mensaje_desct1()
elif tramo == "B" or Tramo =="C":
    if edad <= 30:
        descuent_med = (Medicamentos * 12)//100
        Medicamentos -= descuent_med
        Mensaje_desct1()
    elif edad >= 31 and edad <= 60:
        descuent_med = (Medicamentos * 8)//100
        Medicamentos -= descuent_med
        Mensaje_desct1()
elif edad > 60:
    print("El valor de los medicamentos es: ", Medicamentos)
    

if tramo == "A" or tramo =="B":
    descuent_despa = (despacho * 10)//100
    despacho -= descuent_despa
    print(despacho)
    if edad >= 55:
        descuent_AD = (despacho * 5)//100
        despacho -= descuent_AD
        print(despacho)
    Mensaje_desct2()
elif edad > 60:
    print(despacho)