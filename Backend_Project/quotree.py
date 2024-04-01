from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/quotree'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)

class Quote(db.Model):
    #public_id, quote_text, categories, author_id, source, year, date_post
    id = db.Column(db.Integer, primary_key=True, index=True)
    public_id = db.Column(db.String, nullable=False)
    quote_text = db.Column(db.String(2000), unique = True, nullable=False)
    categories = db.Column(db.String, db.ForeignKey('categories.id'))
    author_id = db.Column(db.String, db.ForeignKey('Author.id'))
    source = db.Column(db.String)
    year = db.Column(db.Integer)
    date_post = db.Column(db.Date)
    author_quote = db.relationship('Author', back_populates='quote')
    categories_quote = db.relationship('Categories', back_populates='quote')
    agree = db.relationship('Agree', back_populates='quote_agree')
    disagree = db.relationship('Disagree', back_populates='quote_disagree')
    
    def __repr__(self):
        return f'<Quote: {self.id}>'
    
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    categories = db.Column(db.String, unique = True, nullable = False)
    quote = db.relationship('Quote', back_populates='categories_quote')
    
    def __repr__(self):
        return f'<Categories: {self.id}>'
    
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    public_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    profession = db.Column(db.String(20), db.ForeignKey('profession.id'))
    country = db.Column(db.String(50), db.ForeignKey('country.id'))
    born = db.Column(db.Date, nullable = False)
    quote = db.relationship('Quote', back_populates='author_quote')
    agree = db.relationship('Agree', back_populates='author_agree')
    disagree = db.relationship('Disagree', back_populates='author_disagree')
    author_profession = db.relationship('Profession', back_populates='author_quote')
    author_country = db.relationship('Country', back_populates='author_quote')
    follows = db.relationship(
    'Author',
    secondary='author_follows',
    primaryjoin=id==db.Table('author_follows').c.follower_id,
    secondaryjoin=id==db.Table('author_follows').c.followed_id,
    backref='followers'
)
    
    def __repr__(self):
        return f'<Author: {self.id}>'

    
class Profession(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    Profession = db.Column(db.String(50), unique=True, nullable = False)
    author_quote = db.relationship('Author', back_populates='author_profession')

    def __repr__(self):
        return f'<Profession: {self.id}>'
    
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    Profession = db.Column(db.String(50), unique=True, nullable = False)
    author_quote = db.relationship('Author', back_populates='author_country')

    def __repr__(self):
        return f'<Country: {self.id}>'
    
class Agree(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    public_id = db.Column(db.String, nullable=False)
    agree_text = db.Column(db.String(10000), unique = True, nullable=False)
    author_id = db.Column(db.String, db.ForeignKey('author.id'))
    quote_id = db.Column(db.String, db.ForeignKey('quote.id'))
    date_post = db.Column(db.Date)
    author_agree = db.relationship('Author', back_populates='agree')
    quote_agree = db.relationship('Quote', back_populates='agree')
    
    def __repr__(self):
        return f'<Agree: {self.id}>'
    
class Disagree(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    public_id = db.Column(db.String, nullable=False)
    disagree_text = db.Column(db.String(10000), unique = True, nullable=False)
    author_id = db.Column(db.String, db.ForeignKey('author.id'))
    quote_id = db.Column(db.String, db.ForeignKey('quote.id'))
    date_post = db.Column(db.Date)
    author_disagree = db.relationship('Author', back_populates='disagree')
    quote_disagree = db.relationship('Quote', back_populates='disagree')
    
    def __repr__(self):
        return f'<Disagree: {self.id}>'
    
from flask_migrate import Migrate
migrate = Migrate(app, db)

@app.route('/')
def home():
    return {
        'message': 'Selamat datang di Quotree.com'
    }
    
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    author = Author.query.filter_by(username=username, password=password).first()
    if author:
        session['author_id'] = author.id
        return jsonify({'message': 'Login berhasil!'})
    else:
        return jsonify({'message': 'Login gagal!'}, 401)

@app.route('/logout')
def logout():
    session.pop('author_id', None)
    return jsonify({'message': 'Logout berhasil!'})


@app.route('/myquote')
def protected():
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    elif 'author_id' in session:
        author_id = session['author_id']
    quotes = Quote.query.filter_by(author_id=author_id).first()
    #public_id, quote_text, categories, author_id, source, year, date_post
    return jsonify([
		{
			'id' : quote.public_id,
            'quote': quote.quote_text,
            'author' : quote.author_id,
            'year' : quote.year,
            'categories' : quote.categories,
            'source' : quote.source,
            'date' : quote.date_post
			} for quote in quotes
	])
    
@app.route('/followquote')
def protected():
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    elif 'author_id' in session:
        author_id = session['author_id']
    author = Author.query.filter_by(id=author_id).first()
    #public_id, quote_text, categories, author_id, source, year, date_post
    return jsonify([
		{
			'id' : quote.public_id,
            'quote': quote.quote_text,
            'author' : quote.author_id,
            'year' : quote.year,
            'categories' : quote.categories,
            'source' : quote.source,
            'date' : quote.date_post
			} for quote in quotes
	])