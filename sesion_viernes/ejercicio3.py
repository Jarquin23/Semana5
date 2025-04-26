print("Presiona Cero para salir")
dia = int(input("Ingrese el día de la semana de forma numérica(1-7)"))
while dia !=0:
    if dia==1:
        print("Lunes")
    if dia==2:
        print("Martes")
    if dia==3:
        print("Miércoles")
    if dia==4:
        print("Jueves")
    if dia==5:
        print("Viernes")
    if dia==6:
        print("Sábado")
    if dia==7:
        print("Domingo")
    else:
        print("Error. El número digitado no es válido")
    print("Presiona Cero para salir")
    dia = int(input("Ingrese el día de la semana de forma numérica(1-7)"))