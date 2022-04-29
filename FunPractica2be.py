def carga_conjunto(limite, conjunto):
    for i in range (1, limite+1):
        num=int(input(f"Ingrese el {i}° numero: "))
        conjunto.add(num)
conj1 = set()
conj2 = set()
lim1 = int(input("Ingrese la cantidad de elementos del Primer Conjunto: "))
carga_conjunto(lim1, conj1)
lim2 = int(input("Ingrese la cantidad de elementos del Segundo Conjunto: "))
carga_conjunto(lim2, conj2)
print(f"Los elementos comunes son: {conj1.intersection(conj2)}")