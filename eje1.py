inversion = int(input("Ingrese el capital que desea invertir: "))
if inversion > 0:

 tasa = (15/100) / 12
 ganancia = inversion * tasa 
 total = inversion + ganancia
 print(f"el monto ganado durante el mes: ${ganancia:.2f}")
else:
    print("el capital de ser mayor que 0: ")



