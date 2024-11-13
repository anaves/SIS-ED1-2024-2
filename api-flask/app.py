from flask import Flask, request
from flask_cors import CORS

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

def dados(cpf):
    dados_pessoas = {
        "12345678900": {
            "nome": "João da Silva",
            "data_nascimento": "1990-05-15",
            "email": "joao.silva@example.com",
        },
        "98765432111": {
            "nome": "Maria Oliveira",
            "data_nascimento": "1985-09-20",
            "email": "maria.oliveira@example.com",
        },
        "11122233344": {
            "nome": "Carlos Pereira",
            "data_nascimento": "1978-02-10",
            "email": "carlos.pereira@example.com",
        },
        "55566677788": {
            "nome": "Ana Costa",
            "data_nascimento": "1995-07-25",
            "email": "ana.costa@example.com",
        },
        "99988877766": {
            "nome": "Paulo Souza",
            "data_nascimento": "2000-11-30",
            "email": "paulo.souza@example.com",
        },
    }
    vazio = {
        "nome": "Nao encontrado",
        "data_nascimento": "Nao encontrado",
        "email": "Nao encontrado",
    }
    cliente = dados_pessoas.get(cpf, vazio)
    return cliente

if __name__ == "__main__":
    app.run(debug=True)
