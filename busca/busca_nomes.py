# biblioteca que permite fazer requisicoes (solicitacoes)
import requests

def busca_ibge():
    url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/"
    response = requests.get(url)
    # print(response)
    resultado = response.json()
    return resultado

if __name__ == "__main__":
    vetor = busca_ibge()
    lista_nomes = []
    for i in range(len(vetor)):
        elemento = vetor[i]
        nome = elemento["nome"]
        lista_nomes.append(nome)
        # print(elemento)
        # print("*********************")
        # print(elemento["nome"])
        # print("---------------------")
    print(lista_nomes)