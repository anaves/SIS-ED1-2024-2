# biblioteca que permite fazer requisicoes (solicitacoes)
import requests
# import time
import busca_sequencial
"""
Exercicio: Buscar os nomes agora da API gerador-nomes e testar a busca sequencial
"""
def busca_nomes(qtd=20):
    url = f"https://gerador-nomes.wolan.net/nomes/{qtd}"
    ## terminar o codigo para recuperar os dados!
    print(url)
    resposta = requests.get(url)
    resultado = resposta.json()
    return resultado

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
    lista_nomes = busca_nomes(50)  
    print(lista_nomes)
    aux = input("Digite o nome pra buscar: ")
    indice = busca_sequencial.busca_sequencial(lista_nomes, aux)
    if indice >= 0:
        print(f"{aux} esta no indice {indice}")
    else:
        print(f"{aux} NAO esta na lista")
