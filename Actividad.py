import random

nombre_usuario = str(input("Introduzca su nombre: "))

tipo_cliente = str(input("Introduzca su nivel de cliente : (Normal - Frecuente - Premium - Empresarial - Adulto Mayor): " ))

monto = int(input("Ingrese el mont total de su compra: $ "))
metodo_pago = input("ingrese el metodo de pago: ").capitalize()

descuento = 0
recargo = 0

tipo_cliente = tipo_cliente.lower()

nombre_minus = nombre_usuario.lower()

if nombre_minus.find("a") !=-1 or nombre_minus.find("e") != -1 or nombre_minus.find("u") != -1:
    descuento += 0.02
    print("Tu Nombre tiene en nuestra tienda ... ¡Felicidades!")

if tipo_cliente == "normal" and monto >= 100000:
    descuento += 0.05
elif tipo_cliente == "frecuente" and monto >= 80000:
    descuento += 0.10
elif tipo_cliente == "Premium" and monto >= 50000:
    descuento += 0.15
elif tipo_cliente == "Empresarial" and monto >= 200000:
    descuento +=   0.20
elif tipo_cliente == "Adulto Mayor" and monto >= 30000:
    descuento += 0.08


  
if metodo_pago == "Efectivo" and monto > 50000:
        descuento += 0.03
elif metodo_pago == "Credito" and monto > 20000:
    recargo += 0.05

numero_aleatorio = random.randint(1,10)

print (f"El numero aletario es: {numero_aleatorio}")

if numero_aleatorio == 7 or numero_aleatorio == 9:
    descuento += 0.05
elif numero_aleatorio == 1 or numero_aleatorio == 2:
    recarga += 0.03
elif numero_aleatorio == 5:
    print("Gano un cupón")

total_compra = monto *(1-descuento + recargo)

print("Resumen de su compra: ")
print (f"Cliente: {nombre_usuario}")
print (f"Método de pago :{metodo_pago}")
print (f"Descuento aplicado: {int(round(descuento*100))}")
print (f"Recargo aplicado: {recargo}") 
