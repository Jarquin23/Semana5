monto = float(input("Ingrese el monto total de la cuenta: "))
satisfaccion = input("¿Cómo fue su experiencia con el servicio? (buena/mala): ")
if satisfaccion== "buena":
    propina = monto * 0.15
elif satisfaccion== "mala":
    propina = monto * 0.05
else:
    propina = 0
    print("Nivel de satisfacción no válido. No se calculará propina.")
total_pago = monto + propina
print(f"Propina: ${propina:.2f}")
print(f"Total a pagar: ${total_pago:.2f}")