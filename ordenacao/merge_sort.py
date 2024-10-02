
def intercala(inicio, meio, fim, lista):
    i = inicio
    j = meio
    lista_ordenada = []
    while i < meio and j < fim:
        if lista[i] < lista[j]:
            lista_ordenada.append(lista[i])
            i = i+1
        else:
            lista_ordenada.append(lista[j])
            j = j+1
    # pq i == meio ou j == fim
    # vamos pegar todos os elementos da primeira metade da lista
    while i < meio:
        lista_ordenada.append(lista[i])
        i = i+1

    while j < fim:
        lista_ordenada.append(lista[j])
        j = j+1
    return lista_ordenada

# main: principal
if __name__ == '__main__':
    valores = [1,3,6,7,0,8,11,12]
    inicio = 0
    fim = len(valores)
    meio = (inicio+fim)//2
    ordenada = intercala(inicio, meio, fim, valores)
    print(ordenada)