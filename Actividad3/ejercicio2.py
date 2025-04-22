inv = int(input("Ingrese la cantidad inicial del inventario: "))
prod_rec = int(input("Ingrese la cantidad de productos recibidos: "))
prod_ven = int(input("Ingrese la cantidad de productos vendidos: "))
suma = prod_rec + inv
inv_act = suma - prod_ven
print(f"El inventario inicial era: {inv}")
print(f"Se recibieron {prod_rec} productos")
print(f"Se vendieron {prod_ven} productos")
print(f"El inventario final es: {inv_act}")