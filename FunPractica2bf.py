def carga_lista(lim, lista):
    for i in range (1, lim+1):
        num=int(input(f"Ingrese el {i}° numero: "))
        lista.append(num)
def convierte_a_conjunto(lista):
    return set(lista)
def carga_conjunto(lim2, conj2):
    for i in range (1, lim2+1):
        num=int(input(f"Ingrese el {i}° numero: "))
        conj2.add(num)
print("Lista a Conjunto: \n")
lim = int(input("Ingrese la cantidad de elementos de la lista: "))
lista = []
carga_lista(lim, lista)
print(f"La lista es: {lista}")
conj = convierte_a_conjunto(lista)
print(f"El conjunto es: {conj}")
conj2 = set()
lim2 = int(input("Ingrese la cantidad de elementos del Segundo Conjunto: "))
carga_conjunto(lim2, conj2)
print(f"El Primer conjunto es: {conj}")
print(f"El Segundo conjunto es: {conj2}")
print(f"La union del Primer y Segundo conjunto es: {conj.union(conj2)}")
print(f"La interseccion del Primer y Segundo conjunto es: {conj.intersection(conj2)}")
print(f"La diferencia del Primer respecto del Segundo conjunto es: {conj.difference(conj2)}")
print(f"El Primer conjunto es igual al Segundo? : {conj==conj2}")