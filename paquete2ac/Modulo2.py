import Modulo1 as fun
n = int(input("Ingrese un numero para ver la secuencia Fibonacci de esa cantidad: ")) 
for i in range(n):
    print(fun.rec_fib(i))