def min_max_de_lista(n1, n2):
    if n1 % 2 != 0:
        n1 += 1
    if n2 % 2 == 0:
        n2 += 1
    print(f"La lista es: {list(range(n1, n2, 2))}")