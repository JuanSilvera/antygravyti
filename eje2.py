base = float(input("Ingrese el sueldo que normal: "))
venta1 = float(input("ingrese el valor de la venta 1: "))
venta2 = float(input("ingrese el valor de la venta 2: "))
venta3 = float(input("ingrese el valor de la venta 3: "))

if base >= 0 and venta1 >= 0 and venta2 >= 0 and venta3 >= 0:
 total_venta = venta1 + venta2 + venta3
 comi = total_venta * 0.10
 recibir = base + comi 
 print(f"la comision fue de: ${comi:.2f}")
 print(f"lo que debe de recibir en el mes: ${recibir:.2f}")
else: 
    print("no seas brutouuu no puedes ganar menos que 0")

