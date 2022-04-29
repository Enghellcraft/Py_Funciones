def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
n = int(input("Ingrese un numero para ver la secuencia Fibonacci de esa cantidad: ")) 
for i in range(n):
    print(rec_fib(i))


   






