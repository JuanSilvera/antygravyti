edad = int(input("Ingresa tu edad: "))

if edad > 0:
    num_pul = (220 - edad) / 10
    print(f"Número de pulsaciones por cada 10 segundos de ejercicio: {num_pul:.1f}")
else:
    print("Ingresa una edad válida.")