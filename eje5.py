pesos = float(input("ingresa la cantidad en pesos: "))
tasa = float(input("ingresa el valor actual de 1 dólar en pesos: "))

if pesos >= 0 and tasa > 0:
    dolares = pesos / tasa
    print(f"equivalencia en dólares: ${dolares:.2f}")
else:
    print("por favor, ingresa valores válidos (la tasa debe ser mayor a 0).")