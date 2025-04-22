cap_in = float(input("Ingrese el capital: "))
int_an = float(input("Ingrese el porcentaje de interés anual: "))
cant_años = int(input("Ingresar la cantidad de años: "))
tasa_dec = int_an / 100
conv = (1 + tasa_dec)** cant_años
monto_final = conv * tasa_dec
interes = monto_final - cap_in
print(f"Inicialmente, su capital tenía un valor de: {cap_in}")
print(f"La tasa de interés tiene un valor del: {int_an}")
print(f"El monto final equivale a: {monto_final}")
print(f"El interés ganado es de: {interes}")