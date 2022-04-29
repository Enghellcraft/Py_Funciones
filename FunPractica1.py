def maximo(a, b):
    if a > b:
        return a
    else:
        return b
def minimo(a, b):
    if a < b:
        return a
    else:
        return b
x = int(input("Ingrese un número:\n"))
y = int(input("Ingrese otro número:\n"))
print(maximo(x-3, minimo(x+2, y-5)))