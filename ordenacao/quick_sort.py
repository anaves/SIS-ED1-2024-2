def quick_particao(lista, esq, dir):
    if len(lista) <= 1:
        return lista
    else:
        indice_pivo = (esq + dir) // 2
        pivo = lista[indice_pivo]
        i = esq
        j = dir
        while True:
            while lista[i] < pivo:  # correcao
                i += 1

            while lista[j] > pivo:  # correcao
                j -= 1
            
            if i >= j: # na posicao do pivo
                return j  # correcao
            
            # troca de posicoes
            lista[i], lista[j] = lista[j], lista[i]
            i += 1 # correcao
            j -= 1 # correcao

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        local_pivo = quick_particao(lista, inicio, fim)
        quick_sort(lista, inicio, local_pivo)
        quick_sort(lista, local_pivo+1, fim)

if __name__ == "__main__":
    vetor = list(range(20, 10, -1))
    print(vetor)
    quick_sort(vetor, 0, len(vetor)-1)
    print(vetor)