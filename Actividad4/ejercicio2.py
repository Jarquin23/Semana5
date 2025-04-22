import datetime as dt
fecha_ingreso = input("Fecha ingreso YYYY-MM-DD")
fecha_ingreso = dt.datetime.strptime(fecha_ingreso, "%Y-%m-%d")
fecha_act = dt.datetime.now()
dias = (fecha_act - fecha_ingreso).days
print(fecha_act)
print(fecha_ingreso)
print("dias", dias)
if dias > 30:
    print("Cuenta inactiva")