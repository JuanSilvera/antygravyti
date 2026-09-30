parcial1 = float(input("ingresa la calificación del parcial 1: "))
parcial2 = float(input("ingresa la calificación del parcial 2: "))
parcial3 = float(input("ingresa la calificación del parcial 3: "))

promedio = (parcial1 + parcial2 + parcial3) / 3
examen_final = float(input("ingresa la calificación del examen final: "))
trabajo_final = float(input("ingresa la calificación del trabajo final: "))

nota_final = (promedio * 0.40) + (examen_final * 0.50) + (trabajo_final * 0.10)
print(f"\ncalificación final: {nota_final:.2f}")

if nota_final >= 3.0:
    print("estado: aprobado")
else:
    print("estado: reprobado")