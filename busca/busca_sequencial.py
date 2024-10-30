vetor = ["quadrado", "circulo", "triangulo invertido", "triangulo", "estrela", "smile"]

def busca_sequencial(vetor, procurado):
  for i in range(len(vetor)):
    if vetor[i] == procurado:
      return i
  return -1

if __name__ == "__main__":
    print(busca_sequencial(vetor, "estrela"))
    resultado = "bola" in vetor
    print(resultado)
