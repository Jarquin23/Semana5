edad = float(input("Dime tu edad: "))
if 0<= edad <=11:
    categoria = "niño"
elif 12 <= edad <= 17:
    categoria = "adolescente"
elif 18 <= edad <= 64:
    categoria = "adulto"
elif edad >=65:
    categoria = "adulto mayor"
else:
    categoria = "Edad no válida"
print(f"La categoría es: {categoria}")