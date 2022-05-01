import Modulo1 as fun
ntop = int(input("Ingrese un limite superior: "))
nbot = int(input("Ingrese un limite inferior: "))
lista = []
fun.add_a_la_lista(lista, nbot, ntop)
print(f"Los numeros ingresados son: {lista}")
