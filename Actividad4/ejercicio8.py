usuario = input("Ingrese su nombre de usuario: ")
clave = input("Ingrese su clave: ")
if usuario == "admin" and clave == "1234admin":
    print("Acceso permitido: ¡Bienvenido, administrador!")
else:
    print("Acceso denegado. Usuario o clave incorrectos.")