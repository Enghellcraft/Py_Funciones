def add_lista (num, lista1):
    for i in range(0, num):
        palabra = input(f"Escriba la {i+1}° palabra: ")
        lista1.append(palabra)
def rev_lista (lista1,lista2):
    for i in reversed(lista1):
        lista2.append(i)