dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
year = int(input("Ingrese el año: "))
if mes==2:
    if dia > 29:
        print("Fecha inválida: Febrero no tiene más de 29 días.")
    else:
        print("Fecha válida.")
elif mes==4 or mes==6 or mes==9 or mes==11:
    if dia>30:
        print("Fecha inválida, este mes solo cuenta con 30 días.")
    else:
        print("Fecha válida.")
elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    if dia>31:
        print("Fecha inválida, este mes solo cuenta con 31 días.")
    else:
        print("Fecha válida.")
else:
    print("Fecha inválida: Mes no reconocido.")