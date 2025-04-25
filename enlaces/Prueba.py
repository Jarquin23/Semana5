class Nodo:
    def __init__(self, valor):
        self.valor = valor  
        self.siguiente = None  #(inicialmente None)

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista empieza vacía
        

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo  # Si la lista está vacía, el nuevo nodo es la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorre la lista hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo  # Enlaza el nuevo nodo al final

    # Insertar un nuevo valor al inicio de la lista
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza  
        self.cabeza = nuevo  # La cabeza ahora es el nuevo nodo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None  # Para llevar el rastro del nodo previo
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente  # Eliminar el nodo en medio o al final
                else:
                    self.cabeza = actual.siguiente  # Eliminar la cabeza
                return True  # Nodo eliminado
            anterior = actual
            actual = actual.siguiente
        return False  # Si no se encuentra el valor

   
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

   
    def longitudLista(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    
    def esta_vacia(self):
        return self.cabeza is None

  
    def imprimir_ultimo(self):
        if not self.cabeza: 
            print("La lista está vacía")
            return
        actual = self.cabeza
        while actual.siguiente:  
            actual = actual.siguiente
        print(f"El último valor de la lista es: {actual.valor}")


if __name__ == "__main__":
    lista = ListaEnlazada()

    
    datos = input("Ingrese los valores a insertar en la lista, separados por espacio: ").split()
    
  
    for dato in datos:
        lista.insertar(int(dato))
    

    lista.imprimir()  
    
    
    valor_inicio = int(input("Ingrese un valor para insertar al inicio de la lista: "))
    lista.insertar_inicio(valor_inicio)
    lista.imprimir()  # Imprimir lista después de la inserción al inicio

    
    valor_buscar = int(input("Ingrese un valor para buscar en la lista: "))
    print(f"Buscar el valor {valor_buscar}: {lista.buscar(valor_buscar)}")  # True o False
    
   
    valor_eliminar = int(input("Ingrese un valor para eliminar de la lista: "))
    if lista.eliminar(valor_eliminar):
        print(f"El valor {valor_eliminar} ha sido eliminado.")
    else:
        print(f"El valor {valor_eliminar} no se encontró.")
    lista.imprimir()  
    
    print(f"La longitud de la lista es: {lista.longitudLista()}")


    print(f"¿Está la lista vacía? {'Sí' if lista.esta_vacia() else 'No'}")


    lista.imprimir_ultimo()