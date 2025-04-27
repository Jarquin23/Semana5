precio_producto = float(input("Ingrese el precio del producto: "))
saldo = float(input("Ingrese su saldo: "))
if saldo>=precio_producto:
    print("Compra permitida.")
else:
    print("Saldo insuficiente.")