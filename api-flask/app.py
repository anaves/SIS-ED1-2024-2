from flask import Flask, request
from flask_cors import CORS
# pip install flask-cors
app = Flask("Minha API")
CORS(app) # Ativa cors
@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/soma")
def soma():
    s = 0
    for i in range(20):
        s += i
    return f"resultado={s}"

#http://127.0.0.1:5000/multi?nome=Jose&varx=8&vary=15
@app.route("/multi", methods=["GET"])
def mult():
    nome = request.args.get("nome")
    x = request.args.get("varx", type=float)
    y = request.args.get("vary") # y sera str
    y = float(y)
    resultado = x * y
    return f"Ola {nome}, o resultado = {resultado}"

if __name__ == "__main__":
    app.run(debug=True)