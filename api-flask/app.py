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


@app.route("/consulta", methods=["GET"])
def consulta_cadastro():
    documento = request.args.get("doc")
    registro = dados(documento)
    return registro

@app.route("/cadastro", methods=["POST"])
def cadastrar():
    payload = request.json
    cpf = payload.get("cpf")
    valores = payload.get("dados")
    salvar_dados(cpf, valores)
    return "dados cadastrados"
           
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
    

   
