lista1 = []
lista2 = []
def add_lista (num):
    for i in range(0, num):
        palabra = input(f"Escriba la {i+1}° palabra: ")
        lista1.append(palabra)
def rev_lista (lista):
    for i in reversed(lista1):
        lista2.append(i)
cant = int(input("Indique la cantidad de palabras: "))
add_lista(cant)
print(lista1)
rev_lista(lista1)
print(lista2)