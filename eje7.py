presion = float(input("ingresa la presión: "))
volumen = float(input("ingresa el volumen: "))
temperatura = float(input("ingresa la temperatura: "))

divisor = 0.37 * (temperatura + 460)

if divisor != 0:
    masa = (presion * volumen) / divisor
    print(f"La masa de aire es: {masa:.4f}")
else:
    print("error")