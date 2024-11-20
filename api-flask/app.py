from flask import Flask, request
from flask_cors import CORS
import json
import os  # operational system

# pip install flask-cors
app = Flask("Minha API")
CORS(app)  # Ativa cors

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/soma")
def soma():
    s = 0
    for i in range(20):
        s += i
    return f"resultado={s}"

# http://127.0.0.1:5000/multi?nome=Jose&varx=8&vary=15
@app.route("/multi", methods=["GET"])
def mult():
    nome = request.args.get("nome")
    x = request.args.get("varx", type=float)
    y = request.args.get("vary")  # y sera str
    y = float(y)
    resultado = x * y
    return f"Ola {nome}, o resultado = {resultado}"


@app.route("/consulta", methods=["GET"])
def consulta_cadastro():
    documento = request.args.get("doc")
    registro = dados(documento)
    return registro

def carregar_arquivo():
    # caminho de onde o arquivo esta salvo
    caminho_arquivo = os.path.realpath("api-flask/dados.json")
    try:
        with open(caminho_arquivo, "r") as arq:
            return json.load(arq)
    except Exception:
        return "Falha ao carregar o arquivo"

def gravar_arquivo(dados):
    caminho_arquivo = os.path.realpath("api-flask/dados.json")
    try:
        with open(caminho_arquivo, "w") as arq:
            json.dump(dados, arq, indent=4)
        return "dados armazenados"
    except Exception:
        return "Falha ao carregar o arquivo"

def salvar_dados(cpf, registro):
    dados_pessoas = carregar_arquivo()
    dados_pessoas[cpf] = registro
    gravar_arquivo(dados_pessoas)

def dados(cpf):
    dados_pessoas = carregar_arquivo()
    vazio = {
        "nome": "Nao encontrado",
        "data_nascimento": "Nao encontrado",
        "email": "Nao encontrado",
    }
    cliente = dados_pessoas.get(cpf, vazio)
    return cliente

if __name__ == "__main__":
    app.run(debug=True)
    
    # pode ser uma ideia para um cadastro!!!
    # valores = {
    #     "nome": "Adolfo Silveira",
    #     "data_nascimento": "2000-07-25",
    #     "email": "adolfo.silveira@example.com"
    # }
    # salvar_dados("11111", valores)
