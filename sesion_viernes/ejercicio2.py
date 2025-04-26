sueldo = float(input("Dime el sueldo: "))
bono = 0
if sueldo >3000:
    bono = sueldo * 0.1
elif sueldo >=1500:
    bono = sueldo * 0.05
else:
    bono = 0
print("No tedrá bono.")
