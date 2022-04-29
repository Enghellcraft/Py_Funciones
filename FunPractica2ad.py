def add_a_la_lista():
    num = int(input(f"Ingrese el numero:"))
    lista.append(num)
    while (num > nbot) and (num < ntop):
        num = int(input(f"Ingrese el numero:"))
        if (num > nbot) and (num < ntop):
            lista.append(num)
ntop = int(input("Ingrese un limite superior: "))
nbot = int(input("Ingrese un limite inferior: "))
lista = []
add_a_la_lista()
print(f"Los numeros ingresados son: {lista}")