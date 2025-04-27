saldo_in = float(input("Ingrese el saldo inicial de su cuenta: "))
print("\nSeleccione una opción:") 
print("1 = Vaciar cuenta.")
print("2 = Depositar.")
print("3 = Retirar.")
opcion = int(input("\nIngrese la opcion deseada: "))
if opcion==1:
    saldo = 0
    print("\nCuenta vaciada")
elif opcion==2:
    deposito = float(input("\nIngrese el monto a depositar: "))
    saldo += deposito
    print(f"\nDeposito realizado. Nuevo saldo: ${saldo:.2f}")
elif opcion==3:
    retiro = float(input("\nIngrese el monto a retirar: "))
    if retiro> saldo:
        print("\nNo dispone del saldo suficiente para realizar el retiro.")
    else:
        saldo -= retiro
        print(f"\nRetiro realizado. Nuevo saldo: ${saldo:.2f}")
else:
    print("\nLa opción no es válida.")
print(f"\nSaldo final de la cuenta: ${saldo:.2f}")