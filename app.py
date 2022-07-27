#importar biblioteca
#flask run comando para rodar
#ctrl c cokmando para parar de rodar o comando
#cuidar com a identação, super importante no python
#FLASK_RUN_HOST - 0.0.0.0  O FLASK SALVA AUTOMATICAMENTE
from flask import Flask, render_template
#importar data de criação
from datetime import datetime

app = Flask("hello")

#CRIAR MOCk
posts = [
    {
        "title": "Meu primeiro post",
        "body" : "Mussum Ipsum, cacilds vidis litro abertis. Em pé sem cair, deitado sem dormir, sentado sem cochilar e fazendo pose.Cevadis im ampola pa arma uma pindureta.Quem num gosta di mé, boa gentis num é.Delegadis gente finis, bibendum egestas augue arcu ut est.",
        "author": "Larissa",
        "created": datetime(2022,7,25)
    },
    {
        "title": "Meu segundo post",
        "body" : "Aqui é o texto do post",
        "author": "Anna",
        "created": datetime(2022,7,26)
    },   
]

#rota da aplicação na pg
@app.route("/")
#@app.route("/hello")
def index(): 
    #renderizar template
    return render_template("index.html", posts=posts)

 #criar outra rota
#@app.route("/meucontato")
#def meuContato():
    #return render_template('index.html', email='didi.ego@gmail.com', nome='Danilo', telefone="98767888")

    @app.route('/login')
    def login():
        return render_template("login.html")