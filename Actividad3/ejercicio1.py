calificacion1 = int(input("Ingrese la clasificación 1: "))
calificacion2 = int(input("Ingrese la calificación 2: "))
calificacion3 = int(input("Ingrese la clasifecación 3: "))
suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3

print(f"""Calificación 1: {calificacion1}
      Calificación 2: {calificacion2}
      Calificación 3: {calificacion3}
      Promedio {promedio:.0f}""")
