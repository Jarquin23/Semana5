temperatura = float(input("Ingrese la temperatura a la que se encuentre su servidor en °C: "))
uso_cpu = float(input("Ingrese el uso del cpu en porcentaje: "))
if temperatura>80 or uso_cpu>95:
    print("¡Protocolo de emergencia activado!")
else:
    print("Condiciones normales.")