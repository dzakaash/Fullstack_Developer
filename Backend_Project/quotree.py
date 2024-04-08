from flask import Flask, request, jsonify, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from sqlalchemy.sql import func

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
    author_id = db.Column(db.String, db.ForeignKey('author.id'))
    source = db.Column(db.String)
    year = db.Column(db.Integer)
    date_post = db.Column(db.Date)
    #relation
    author_quote = db.relationship('Author', back_populates='quote')
    categories_quote = db.relationship('Categories', back_populates='quote')
    agree = db.relationship('Agree', back_populates='quote_agree')
    disagree = db.relationship('Disagree', back_populates='quote_disagree')
    
    def __repr__(self):
        return f'<Quote: {self.id}>'
    
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    categories = db.Column(db.String, unique = True, nullable = False)
    #relation
    quote = db.relationship('Quote', back_populates='categories_quote')
    author = db.relationship('Author', back_populates='favorite_categories')
    
    def __repr__(self):
        return f'<Categories: {self.id}>'
    
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    public_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(128), nullable=False)
    profession = db.Column(db.String(20), db.ForeignKey('profession.id'))
    country = db.Column(db.String(50), db.ForeignKey('country.id'))
    born = db.Column(db.Date, nullable = False)
    #relation
    quote = db.relationship('Quote', back_populates='author_quote')
    agree = db.relationship('Agree', back_populates='author_agree')
    disagree = db.relationship('Disagree', back_populates='author_disagree')
    author_profession = db.relationship('Profession', back_populates='author_quote')
    author_country = db.relationship('Country', back_populates='author_quote')
    favorite_categories = db.relationship('Categories', back_populates='author')
    #relation self
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
    #relation
    author_quote = db.relationship('Author', back_populates='author_profession')

    def __repr__(self):
        return f'<Profession: {self.id}>'
    
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    Profession = db.Column(db.String(50), unique=True, nullable = False)
    #relation
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
    #relation
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
    #relation
    author_disagree = db.relationship('Author', back_populates='disagree')
    quote_disagree = db.relationship('Quote', back_populates='disagree')
    
    def __repr__(self):
        return f'<Disagree: {self.id}>'
    
from flask_migrate import Migrate
migrate = Migrate(app, db)

#0. Home
@app.route('/')
def home():
    return {
        'message': 'Selamat datang di Quotree.com'
    }
    
#1. Login
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    author = Author.query.filter_by(username=auth.username, password=auth.password).first()
    if author and check_password_hash(author.password, auth.password):
        session['author_id'] = author.id
        return jsonify({'message': 'Login berhasil!'})
    else:
        return jsonify({'message': 'Login gagal!'}, 401)

#2. Logout
@app.route('/logout')
def logout():
    session.pop('author_id', None)
    return jsonify({'message': 'Logout berhasil!'})

#3. Sign-Up Author
@app.route('/signup', methods=['POST'])
def signup():
    #json 'name', 'email, 'password', confirm_password', 'profession', 'country', 'born'
    data = request.get_json()
    # Mendapatkan data dari request
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    profession = data.get('profession')
    country = data.get('country')
    born = data.get('born')
    # Verifikasi bahwa password dan konfirmasi password sama
    if password != confirm_password:
        return jsonify({'message': 'Password dan konfirmasi password tidak cocok'}), 400
    # Hash password sebelum disimpan ke database
    hashed_password = generate_password_hash(password, method='sha256')
    # Membuat author baru
    new_author = Author(
        name=name,
        email=email,
        password=hashed_password,
        profession=profession,
        country=country,
        born=born
    )
    # Menyimpan author ke database
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': 'Pendaftaran berhasil, Silahkan Login'}), 201

#4. Melihat profil Author sendiri 
@app.route('/profile', methods=['GET'])
def view_profile():
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    author_id = session['author_id']
    # Mendapatkan informasi tentang author dari database
    author = Author.query.get(author_id)
    return jsonify({
        'name': author.name,
        'email': author.email,
        'profession': author.profession,
        'country': author.country,
        'born': author.born.strftime('%Y-%m-%d'),
        'quote_count': len(author.quote),
        'following_count': len(author.follows),
        'followers_count': len(author.followers)
    })

#5. Membuat Quote
@app.route('/quote/create', methods=['POST'])
def create_quote():
    #json 'quote_text', 'categories', 'source', 'year'
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    author_id = session['author_id']
    # Mendapatkan data kutipan dari request
    data = request.get_json()
    quote_text = data.get('quote_text')
    categories = data.get('categories')
    source = data.get('source')
    year = data.get('year')
    # Membuat ID publik untuk kutipan baru
    public_id = str(uuid.uuid4())
    # Mendapatkan tanggal saat ini
    date_post = datetime.now().date()
    # Membuat kutipan baru
    new_quote = Quote(
        public_id=public_id,
        quote_text=quote_text,
        categories=categories,
        author_id=author_id,
        source=source,
        year=year,
        date_post=date_post
    )
    # Menyimpan kutipan baru ke dalam database
    db.session.add(new_quote)
    db.session.commit()
    return jsonify({
    'id': new_quote.public_id,
    'quote': new_quote.quote_text,
    'author': new_quote.author_id,
    'year': new_quote.year,
    'categories': new_quote.categories,
    'source': new_quote.source,
    'date': new_quote.date_post.strftime('%Y-%m-%d'),
    'agree': len(new_quote.agree),
    'disagree': len(new_quote.disagree)
})

#6. Melihat daftar Quote yang dia tulis, diurutkan dari yang terbaru
@app.route('/quote/myquote')
def view_myquote():
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    author_id = session['author_id']
    quotes = Quote.query.filter_by(author_id=author_id).order_by(Quote.date_post.desc()).all()
    #public_id, quote_text, categories, author_id, source, year, date_post
    return jsonify([
		{
			'id' : quote.public_id,
            'quote': quote.quote_text,
            'author' : quote.author_id,
            'year' : quote.year,
            'categories' : quote.categories,
            'source' : quote.source,
            'date' : quote.date_post,
			'agree': len(quote.agree),
            'disagree': len(quote.disagree)
		} for quote in quotes
	])
    
#7. Melihat profil author lain
@app.route('/profile/<author_id>', methods=['GET'])
def view_author(author_id):
    # Memeriksa apakah author dengan ID yang diberikan ada dalam database
    author = Author.query.get(author_id)
    if author is None:
        return jsonify({'message': 'Author tidak ditemukan'}), 404
    # Mengonversi informasi author ke dalam format JSON
    return jsonify({
        'name': author.name,
        'email': author.email,
        'profession': author.profession,
        'country': author.country,
        'born': author.born.strftime('%Y-%m-%d'),  # Mengonversi tanggal lahir ke dalam format yang diinginkan
        'quote_count': len(author.quote),
        'following_count': len(author.follows),
        'followers_count': len(author.followers)
    })
    
# 8. Melihat Quote author lain
@app.route('/quote/<author_id>', methods=['GET'])
def view_author_quotes(author_id):
    # Memeriksa apakah author dengan ID yang diberikan ada dalam database
    author = Author.query.get(author_id)
    if author is None:
        return jsonify({'message': 'Author tidak ditemukan'}), 404
    # Mengumpulkan semua quote yang ditulis oleh author dengan ID yang diberikan
    quotes = Quote.query.filter_by(author_id=author_id).order_by(Quote.date_post.desc()).all()
    return jsonify([
		{
			'id' : quote.public_id,
            'quote': quote.quote_text,
            'author' : quote.author_id,
            'year' : quote.year,
            'categories' : quote.categories,
            'source' : quote.source,
            'date' : quote.date_post,
			'agree': len(quote.agree),
            'disagree': len(quote.disagree)
		} for quote in quotes
	])

#9. Mengikuti Author lain
@app.route('/follow/<int:author_id>', methods=['POST'])
# membuat fitur follow author lain
#  json 'follower_id'
def follow_author(author_id):
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    follower_id = session['author_id']
    # Mencari author yang diikuti dan yang akan mengikutinya
    followed_author = Author.query.get(author_id)
    follower_author = Author.query.get(follower_id)
    # Memastikan author yang diikuti dan pengikutnya ada di database
    if followed_author is None or follower_author is None:
        return jsonify({'message': 'Author tidak ditemukan!'}), 404
    # Memastikan author tidak mengikuti dirinya sendiri
    if followed_author == follower_author:
        return jsonify({'message': 'Tidak dapat mengikuti diri sendiri!'}), 400
    # Memastikan pengikut tidak mengikuti author yang sama lagi
    if followed_author in follower_author.follows:
        return jsonify({'message': 'Anda sudah mengikuti author ini!'}), 400
    # Menambahkan author yang diikuti ke daftar pengikut
    follower_author.follows.append(followed_author)
    db.session.commit()
    return jsonify({'message': 'Berhasil mengikuti author!'})

# 10. Mengunfoll Author lain
@app.route('/unfollow/<author_id>', methods=['DELETE'])
def unfollow_author(author_id):
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    follower_id = session['author_id']
    # Memeriksa apakah author yang sedang login sudah mem-follow author yang akan di-unfollow
    if not Author.query.filter_by(id=follower_id).first().follows.filter_by(id=author_id).first():
        return jsonify({'message': 'Kamu belum mem-follow author tersebut'}), 400
    # Menghapus relasi follow antara author yang sedang login dengan author yang akan di-unfollow
    Author.query.get(follower_id).follows.remove(Author.query.get(author_id))
    db.session.commit()
    return jsonify({'message': 'Unfollow berhasil'}), 200

#11. Melihat Page Quote yang berisi Quote dari penulis yang dia ikuti, diurutkan berdasarkan date posting dari yang terbaru
@app.route('/quotes/follow/<int:page_number>', methods=['GET'])
def get_quotes(page_number):
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    author_id = session['author_id']
    # Mencari author
    author = Author.query.get(author_id)
    # Mengumpulkan semua quote dari author yang diikuti
    quotes = []
    per_page = 1  # Jumlah kutipan per halaman
    for followed_author in author.follows:
        quotes.extend(followed_author.quote)
    # Mengurutkan kutipan berdasarkan tanggal posting dari yang terbaru
    sorted_quotes = sorted(quotes, key=lambda x: x.date_post, reverse=True)
    # Melakukan paginasi untuk membatasi jumlah kutipan yang ditampilkan per halaman
    start_index = (page_number - 1) * per_page
    end_index = start_index + per_page
    paginated_quotes = sorted_quotes[start_index:end_index]
    return jsonify([
    {
        'id': quote.public_id,
        'quote': quote.quote_text,
        'author': quote.author_id,
        'year': quote.year,
        'categories': quote.categories,
        'source': quote.source,
        'date': quote.date_post,
        'agree': len(quote.agree),
        'disagree': len(quote.disagree)
    } for quote in paginated_quotes
])
    
#12. Melihat Page Quote dari kategori yang dia suka, diacak secara random urutannya, yang ditampilkan hanya dari yang belum dia agree atau disagree
@app.route('/quotes/daily', methods=['GET'])
def daily_quote():
    if 'author_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    author_id = session['author_id']
    # Mengambil author dari database
    author = Author.query.get(author_id)
    # Mengambil kategori-kategori yang diikuti oleh author
    followed_categories = author.categories
    # Mengambil quote acak dari kategori-kategori yang diikuti oleh author
    random_quote = Quote.query.filter(Quote.categories.in_(followed_categories)).\
        filter(~Quote.agree.any(author_id=author_id) & ~Quote.disagree.any(author_id=author_id)).\
        order_by(func.random()).first()
    if random_quote is None:
        return jsonify({'message': 'Tidak ada kutipan yang tersedia'}), 404
    # Mengonversi informasi quote ke dalam format JSON
    return jsonify({
        'id': random_quote.public_id,
        'quote': random_quote.quote_text,
        'author': random_quote.author_id,
        'year': random_quote.year,
        'categories': random_quote.categories,
        'source': random_quote.source,
        'date': random_quote.date_post.strftime('%Y-%m-%d'),
        'agree': len(random_quote.agree),
        'disagree': len(random_quote.disagree)
    })
    
# 13. Melihat Quote trending, diurutkan dari yang paling banyak agree atau disagree nya
@app.route('/quotes/trending/<int:page_number>', methods=['GET'])
def get_trending_quotes(page_number=1):
    per_page = 10  # Jumlah kutipan per halaman
    # Mendapatkan kutipan yang paling banyak disetujui (agree) atau tidak disetujui (disagree)
    # Diurutkan berdasarkan jumlah agree atau disagree dalam urutan menurun
    trending_quotes = Quote.query \
        .outerjoin(Agree).outerjoin(Disagree) \
        .group_by(Quote.id) \
        .order_by(func.count(Agree.id).desc(), func.count(Disagree.id).desc()) \
        .paginate(page_number, per_page, error_out=False)
    # Mengonversi hasil ke dalam format JSON
    if trending_quotes.items:
        return jsonify({
            'quotes': [{
                'id': quote.public_id,
                'quote': quote.quote_text,
                'author': quote.author_id,
                'year': quote.year,
                'categories': quote.categories,
                'source': quote.source,
                'date': quote.date_post.strftime('%Y-%m-%d'),
                'agree': len(quote.agree),
                'disagree': len(quote.disagree)
            } for quote in trending_quotes.items]
        })
    else:
        return jsonify({'message': 'Tidak ada kutipan yang tersedia'}), 404
    
# 14.  Melihat daftar penulis berdasarkan profesi tertentu, dan diurutkan bersarkan paling banyak followersnya. satu page memiliki limit menampilkan 10 author.
@app.route('/<profession>/<int:page>', methods=['GET'])
def authors_by_profession(profession, page):
    # Mengambil daftar penulis berdasarkan profesi tertentu, diurutkan berdasarkan jumlah followersnya
    authors = Author.query.filter_by(profession=profession)\
                          .order_by(func.count(Author.followers).desc())\
                          .paginate(page, per_page=10, error_out=False)
    if not authors.items:
        return jsonify({'message': 'Tidak ada penulis dengan profesi tersebut'}), 404
    # Format data penulis ke dalam JSON
    author_list = []
    for author in authors.items:
        author_data = {
            'id': author.public_id,
            'name': author.name,
            'email': author.email,
            'profession': author.profession,
            'country': author.country,
            'born': author.born.strftime('%Y-%m-%d'),
            'follower_count': len(author.followers)
        }
        author_list.append(author_data)
    # Membuat URL untuk halaman selanjutnya jika ada
    next_page = None
    if authors.has_next:
        next_page = url_for('authors_by_profession', profession=profession, page=authors.next_num, _external=True)
    return jsonify({'authors': author_list, 'total_pages': authors.pages, 'next_page': next_page})

# 15.  Melihat daftar penulis berdasarkan negara tertentu, dan diurutkan bersarkan paling banyak followersnya. satu page memiliki limit menampilkan 10 author.
@app.route('/<country>/<int:page>', methods=['GET'])
def authors_by_country(country, page):
    # Mengambil daftar penulis berdasarkan negara tertentu, diurutkan berdasarkan jumlah followersnya
    authors = Author.query.filter_by(country=country)\
                          .order_by(func.count(Author.followers).desc())\
                          .paginate(page, per_page=10, error_out=False)
    if not authors.items:
        return jsonify({'message': 'Tidak ada penulis dengan negara tersebut'}), 404
    # Format data penulis ke dalam JSON
    author_list = []
    for author in authors.items:
        author_data = {
            'id': author.public_id,
            'name': author.name,
            'email': author.email,
            'profession': author.profession,
            'country': author.country,
            'born': author.born.strftime('%Y-%m-%d'),
            'follower_count': len(author.followers)
        }
        author_list.append(author_data)
    # Membuat URL untuk halaman selanjutnya jika ada
    next_page = None
    if authors.has_next:
        next_page = url_for('authors_by_country', country=country, page=authors.next_num, _external=True)
    return jsonify({'authors': author_list, 'total_pages': authors.pages, 'next_page': next_page})