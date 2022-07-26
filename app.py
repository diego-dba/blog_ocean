#importar biblioteca
#flask run comando para rodar
#ctrl c cokmando para parar de rodar o comando
#cuidar com a identação, super importante no python
#FLASK_RUN_HOST - 0.0.0.0  O FLASK SALVA AUTOMATICAMENTE
from flask import Flask, render_template

app = Flask("hello")

#rota da aplicação na pg
@app.route("/")
@app.route("/hello")
def hello(): 
    return "Hello World"

 #criar outra rota
@app.route("/meucontato")
def meuContato():
    return render_template('index.html')