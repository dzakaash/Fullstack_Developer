from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345678@localhost/postgres'

db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(28), nullable=False, unique=True)
    public_id = db.Column(db.String, nullable=False)
    todos=db.relationship('Todo', backref='owner', lazy='dynamic')