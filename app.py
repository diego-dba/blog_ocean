
from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "pudim"


db = SQLAlchemy(app)

#criar classes do Mock, ou seja, o banco de dados
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.String(500))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True) 
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        

db.create_all()
     #rota da aplicação na pg

@app.route("/")
def index(): 
    #renderizar template
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


#@app.route('/login')
#def login():
#        Post.query.all()  #pra devolver todos os posts
#        return render_template("login.html"

#criar outra rota
#@app.route("/meucontato")
#def meuContato():
    #return render_template('index.html', email='didi.ego@gmail.com', nome='Danilo', telefone="98767888")


