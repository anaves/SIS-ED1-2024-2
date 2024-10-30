# biblioteca que permite fazer requisicoes (solicitacoes)
import requests
# import time
import busca_sequencial
"""
Exercicio: Buscar os nomes agora da API gerador-nomes e testar a busca sequencial
"""
def busca_nomes():
    url = "https://gerador-nomes.wolan.net/nomes/100"
    ## terminar o codigo para recuperar os dados!

def busca_ibge():
    url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/"
    response = requests.get(url)
    # print(response)
    resultado = response.json()

    lista_nomes = []
    for i in range(len(resultado)):
        elemento = resultado[i]
        nome = elemento["nome"]
        lista_nomes.append(nome)

    return lista_nomes

if __name__ == "__main__":
    lista_nomes = busca_nomes()  
    print(lista_nomes)
    aux = "RAFAEL"
    indice = busca_sequencial.busca_sequencial(lista_nomes, aux)
    if indice >= 0:
        print(f"{aux} esta no indice {indice}")
    else:
        print(f"{aux} NAO esta na lista")
