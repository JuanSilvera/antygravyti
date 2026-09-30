total = float(input("ingrese el total de lo que va a comprar: "))
if total > 0: 
    descu = total * 0.15
    total_pagar = total - descu
    pago = total_pagar

    total = print("su descuento aplicado en compra queda: ", pago)
else:
    print("el valor debe ser mayor a 0")
