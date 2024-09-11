def soma(n, k):
    # caso base
    if n == 1:
        return k
    else:
        # chamada recursiva
        return k**n + soma(n-1, k)

resultado = soma(100, 3)
print(resultado)