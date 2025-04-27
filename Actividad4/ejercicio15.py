puntaje = float(input("Dime tu calificación: "))
if puntaje <0 or puntaje >10:
    print("Error: Los puntos deben estar entre 0 y 10")
elif 9<= puntaje <=10:
    print("Excelente")
elif 7<= puntaje <=8:
    print("Bueno")
elif 5<= puntaje <=6:
    print("Regular")
elif puntaje <5:
    print("Deficiente")