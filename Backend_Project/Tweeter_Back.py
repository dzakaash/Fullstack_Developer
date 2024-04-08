from flask import Flask, request, jsonify, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/twiter'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)

# 1. Twit : id, public_id, twit_text, user_id, date_post
class Twit(db.Model) :
  id = db.Column(db.Integer, primary_key=True, index=True)
  public_id = db.Column(db.String, nullable=False)
  twit_text = db.Column(db.String(280), nullable=False)
  user_id = db.Column(db.String, db.ForeignKey("user.id"), nullable=False)
  date = db.Column(db.Date)
  like = db.Column(db.Integer, default=0)
  # relation
  user_twit = db.relationship('User', back_populates='twit')
  comment_twit = db.relationship('Comment', back_populates='twit')
  #relation self
  retweeted_by = db.relationship('User', secondary='retweets', backref=db.backref('retweets', lazy='dynamic'))

  def __repr__(self):
    return f'<Twit: {self.twit_text}>'

retweets = db.Table('retweets',
    db.Column('retweet_id', db.Integer, db.ForeignKey('twits.id'), primary_key=True),
    db.Column('retweeted_id', db.Integer, db.ForeignKey('twits.id'), primary_key=True)
)

# 2. User : id, username, front_name, back_name, password, email, born_year, birth_month, birth_day
class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True, index=True)
  username = db.Column(db.String, nullable=False)
  front_name = db.Column(db.String, nullable=False)
  back_name = db.Column(db.String, nullable=False)
  password = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  date_birth = db.Column(db.String, nullable=False)
  # relation
  twit = db.relationship('Twit', back_populates='user_twit')
  user_comment = db.relationship('comment', back_populates='user')
  #relation self
  follows = db.relationship(
  'User',
  secondary='user_follows',
  primaryjoin=id==db.Table('user_follows').c.follower_id,
  secondaryjoin=id==db.Table('user_follows').c.followed_id,
  backref='followers'
)
  
  def __repr__(self):
    return f'<User: {self.username}>'
  
# 3. Comment : id, public_id, comment_text, user_id, twit_id, date_post
class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True, index=True)
  public_id = db.Column(db.String, nullabel=False)
  comment_text = db.Column(db.String(280), nullable=False)
  user_id = db.Column(db.String, db.ForeignKey("user.id"), nullable=False)
  twit_id = db.Column(db.String, db.ForeignKey("twit.id"), nullable=False)
  date_post = db.Column(db.Date)
  like = db.Column(db.Integer, default=0)
  # relation
  twit = db.relationship('Twit', back_populates='comment_twit')
  user = db.relationship('User', back_populates='user_comment')
  
  def __repr__(self):
        return f'<Comment: {self.comment_text}>'
      
from flask_migrate import Migrate
migrate = Migrate(app, db)
####################################

# 0. Welcome
@app.route('/')
def home():
    return {
    'message': 'Selamat datang di Twiter, silahkan login atau register'
    }

# 1. Register New Account
@app.route('/register', method=['POST'])
def register():
#json 'username', 'front_name', 'back_name', 'email, 'password', 'date_birth'
    data = request.get_json()
    # Mendapatkan data dari request
    username = data.get('username')
    front_name = data.get('front_name')
    back_name = data.get('back_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    date_birth = data.get('date_birth')
    # Verifikasi bahwa password dan konfirmasi password sama
    if password != confirm_password:
        return jsonify({'message': 'Password dan konfirmasi password tidak cocok'}), 400
    # Hash password sebelum disimpan ke database
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    # Membuat author baru
    try:
      new_user = Users(
          username=username,
          front_name=front_name,
          back_name=back_name,
          email=email,
          password=hashed_password,
          date_birth=date_birth
      )
      # Menyimpan author ke database
      db.session.add(new_user)
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    return jsonify({'message': 'Pendaftaran berhasil, Silahkan Login'}), 201

#1.1 Login
@app.route('/login', methods=['POST'])
def login():
    try:
      auth = request.authorization
      user = Users.query.filter_by(username=auth.username).first()
      if user and check_password_hash(user.password, auth.password):
          session['user_id'] = user.id
          return jsonify({'message': 'Login berhasil!'})
      else:
          return jsonify({'message': 'Login gagal!'}, 401)
    except Exception as e:
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    
#1.2 Logout
@app.route('/logout')
def logout():
    try:
      session.pop('admin_id', None)
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    return jsonify({'message': 'Logout berhasil!'})
  
# 2. Update User data
@app.route('/profup', method=['PUT'])
def profile_update():
#json 'username', 'front_name', 'back_name', 'email, 'password', 'date_birth'
    data = request.get_json()
    # Mendapatkan data dari request
    username = data.get('username')
    front_name = data.get('front_name')
    back_name = data.get('back_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    date_birth = data.get('date_birth')
    # Verifikasi bahwa password dan konfirmasi password sama
    if password != confirm_password:
        return jsonify({'message': 'Password dan konfirmasi password tidak cocok'}), 400
    try:
      # Mengupdate user data
      user = Users.query.filter_by(username=username).first()
      if not user:
            return jsonify({'message': 'Pengguna tidak ditemukan'}), 404
      if username :
        user.username = username
      if front_name :
        user.front_name = front_name
      if back_name :
        user.back_name = back_name
      if email :
        user.email = email
      if date_birth :
        user.date_birth = date_birth
      if password :
        # Hash password sebelum disimpan ke database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user.password = hashed_password
      # Menyimpan author ke database
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    return jsonify({'message': 'Update profile berhasil!'}), 201
  
# 3. Search User
@app.route('/', methods=['GET'])
def search_by_keywords():
    keywords = request.args.get('keywords')  # Menggunakan request.args untuk mendapatkan parameter dari query string
    if not keywords:
        return jsonify({'message': 'Kata kunci tidak ditemukan'}), 400
    # Memisahkan kata kunci menjadi daftar kata kunci terpisah
    keyword_list = keywords.split()
    try:
        # Mencari pengguna berdasarkan kata kunci dalam username, front_name, atau back_name
        users = Users.query.filter(
            Users.username.ilike('%{}%'.format(keyword_list[0])),
            Users.front_name.ilike('%{}%'.format(keyword_list[0])),
            Users.back_name.ilike('%{}%'.format(keyword_list[0]))
        )
        # Jika terdapat kata kunci tambahan, tambahkan filter untuk setiap kata kunci, menggunkan iterasi
        for keyword in keyword_list[1:]:
            users = users.filter(
                Users.username.ilike('%{}%'.format(keyword)),
                Users.front_name.ilike('%{}%'.format(keyword)),
                Users.back_name.ilike('%{}%'.format(keyword))
            )
        # Memuat hasil pencarian ke dalam objek paginasi
        page = request.args.get('page', 1, type=int)
        per_page = 10
        users_paginated = users.order_by(Users.followers.desc()).paginate(page, per_page, error_out=False)
        # Membuat daftar pengguna dari hasil paginasi
        users_list = []
        for user in users_paginated.items:
            user_data = {
                'username': user.username,
                'front_name': user.front_name,
                'back_name': user.back_name,
                }
            users_list.append(user_data)
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if users_paginated.has_next:
            next_page = url_for('search_by_keywords', keywords=keywords, page=users_paginated.next_num, _external=True)
        return jsonify({'users': users_list, 'total_pages': users_paginated.pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengguna', 'error': str(e)}), 500

# 4. Follow a User
@app.route('/<username>/follow', methods=['POST'])
# membuat fitur follow user lain
#  json 'follower_id'
def follow_user(username):
    if 'user_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    follower_id = session['user_id']
    # Mencari author yang diikuti dan yang akan mengikutinya
    followed_user = Users.query.get(username)
    follower_user = Users.query.get(follower_id)
    # Memastikan user yang diikuti dan pengikutnya ada di database
    if followed_user is None or follower_user is None:
        return jsonify({'message': 'User tidak ditemukan!'}), 404
    # Memastikan author tidak mengikuti dirinya sendiri
    if followed_user == follower_user:
        return jsonify({'message': 'Tidak dapat mengikuti diri sendiri!'}), 400
    try:
      # Memastikan pengikut tidak mengikuti author yang sama lagi
      if followed_user in follower_user.follows:
          return jsonify({f'Anda sudah mengikuti {followed_user.username}!'}), 400
      # Menambahkan author yang diikuti ke daftar pengikut
      follower_user.follows.append(followed_user)
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    return jsonify({f'Berhasil mengikuti {followed_user.username}!'})

# 5. Unfollow a User
@app.route('/<username>/unfollow', methods=['DELETE'])
def unfollow_user(username):
    if 'user_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
    }
    follower_id = session['user_id']
    # Memeriksa apakah user yang sedang login sudah mem-follow user yang akan di-unfollow
    if not Users.query.filter_by(id=follower_id).first().follows.filter_by(username=username).first():
        return jsonify({f'Kamu belum mem-follow {username}'}), 400
    try:
      # Menghapus relasi follow antara user yang sedang login dengan user yang akan di-unfollow
      Users.query.get(follower_id).follows.remove(Users.query.get(username))
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    return jsonify({'message': 'Unfollow berhasil'}), 200

# 6 Get User profile
@app.route('/<username>', methods=['GET'])
def user_profile(username):
    # Memeriksa apakah user dengan username yang diberikan ada dalam database
    user = Users.query.get(username)
    if user is None:
        return jsonify({'message': 'User tidak ditemukan'}), 404
    # Mengonversi informasi author ke dalam format JSON
    return jsonify({
                'id': user.id,
                'username': user.username,
                'front_name': user.front_name,
                'back_name': user.back_name,
                'email': user.email,
                'date_birth': user.date_birth,
                'user_count': len(user.quote),
                'following_count': len(user.follows),
                'followers_count': len(user.followers)
            })

# 7. Get Follower from a user
@app.route('/<username>/followers', methods=['GET'])
def user_followers(username):
    try:
        # Memeriksa apakah pengguna dengan nama pengguna yang diberikan ada dalam database
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return jsonify({'message': 'Pengguna tidak ditemukan'}), 404
        # Mengambil daftar pengguna yang mengikuti pengguna dengan nama pengguna yang diberikan
        followers = user.followers
        # Menggunakan pagination untuk membatasi jumlah pengguna yang ditampilkan per halaman
        page = request.args.get('page', 1, type=int)
        per_page = 10
        followers_paginated = followers.paginate(page, per_page, error_out=False)
        # Memuat data pengguna ke dalam format yang sesuai
        followers_list = []
        for follower in followers_paginated.items:
            follower_data = {
                'username': follower.username,
                'front_name': follower.front_name,
                'back_name': follower.back_name,
            }
            followers_list.append(follower_data)
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if followers_paginated.has_next:
            next_page = url_for('user_followers', username=username, page=followers_paginated.next_num, _external=True)
        return jsonify({'followers': followers_list, 'total_pages': followers_paginated.pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengikut', 'error': str(e)}), 500
      
# 8. Get User's following
@app.route('/<username>/followed', methods=['GET'])
def user_followed(username):
    try:
        # Memeriksa apakah pengguna dengan nama pengguna yang diberikan ada dalam database
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return jsonify({'message': 'Pengguna tidak ditemukan'}), 404
        # Mengambil daftar pengguna yang diikuti oleh pengguna dengan nama pengguna yang diberikan
        followed_users = user.follows
        # Menggunakan pagination untuk membatasi jumlah pengguna yang ditampilkan per halaman
        page = request.args.get('page', 1, type=int)
        per_page = 10
        followed_users_paginated = followed_users.paginate(page, per_page, error_out=False)
        # Memuat data pengguna ke dalam format yang sesuai
        followed_list = []
        for followed_user in followed_users_paginated.items:
            followed_data = {
                'username': followed_user.username,
                'front_name': followed_user.front_name,
                'back_name': followed_user.back_name,
            }
            followed_list.append(followed_data)
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if followed_users_paginated.has_next:
            next_page = url_for('user_followed', username=username, page=followed_users_paginated.next_num, _external=True)
        return jsonify({'followed': followed_list, 'total_pages': followed_users_paginated.pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengguna yang diikuti', 'error': str(e)}), 500

# 9.1 Post a Tweet
@app.route('/twit/create', methods=['POST'])
def create_twit():
    try:
        #json 'twit_text'
        if 'user_id' not in session:
            return {
            'message': 'Kamu belum log-in, silahkan melakukan login'
        }
        user_id = session['user_id']
        # Mendapatkan data twit dari request
        data = request.get_json()
        twit_text = data.get('twit_text')
        # Membuat ID publik untuk kutipan baru
        public_id = str(uuid.uuid4())
        # Mendapatkan tanggal saat ini
        date_post = datetime.now().date()
        # Membuat kutipan baru
        new_twit = Twit(
            public_id=public_id,
            twit_text=twit_text,
            user_id=user_id,
            date_post=date_post
        )
        # Menyimpan kutipan baru ke dalam database
        db.session.add(new_twit)
        db.session.commit()
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    return jsonify({
    'id': new_twit.public_id,
    'twit': new_twit.twit_text,
    'username': new_twit.user_id,
    'date': new_twit.date_post.strftime('%Y-%m-%d'),
    'likes': new_twit.likes,
})
    
# 9.2 Post a Retweet
@app.route('/twit/retweet/<twit_id>', methods=['POST'])
def create_retweet(twit_id):
    try:
        # Periksa apakah pengguna telah masuk
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum masuk, silakan masuk terlebih dahulu'}), 401
        # Mendapatkan user_id dari session
        user_id = session['user_id']
        # Mendapatkan data twit dari request
        data = request.get_json()
        twit_text = data.get('twit_text')
        # Mendapatkan tanggal saat ini
        date_post = datetime.now().date()
        # Membuat ID publik untuk retweet baru
        public_id = str(uuid.uuid4())
        # Membuat retweet baru
        new_retweet = Twit(
            public_id=public_id,
            twit_text=twit_text,
            user_id=user_id,
            date_post=date_post
        )
        # Menyimpan retweet baru ke dalam database
        db.session.add(new_retweet)
        db.session.commit()
        # Temukan twit yang akan diretweet
        twit_to_retweet = Twit.query.filter_by(public_id=twit_id).first()
        # Menambahkan retweet ke twit yang akan diretweet
        twit_to_retweet.retweeteds.append(new_retweet)
        db.session.commit()
        # Format data retweet ke dalam format JSON untuk ditampilkan sebagai respons
        retweet_data = {
            'id': new_retweet.public_id,
            'twit': new_retweet.twit_text,
            'username': new_retweet.user_id,
            'date': new_retweet.date_post.strftime('%Y-%m-%d'),
            'likes': new_retweet.likes,
            'retweet': twit_to_retweet.public_id
        }
        return jsonify(retweet_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat membuat retweet', 'error': str(e)}), 500

# 10. Search Tweet
@app.route('/twit/', methods=['GET'])
def twits_by_keywords():
    try:
        keywords = request.args.get('keywords')  # Menggunakan request.args untuk mendapatkan parameter dari query string
        if not keywords:
            return jsonify({'message': 'Kata kunci untuk pencarian twit tidak ditemukan'}), 400
        # Memisahkan kata kunci menjadi daftar kata kunci terpisah
        keyword_list = keywords.split()
        # Membuat query untuk mencari twit berdasarkan kata kunci
        twits = Twit.query
        for keyword in keyword_list:
            twits = twits.filter(
                Twit.twit_text.ilike(f'%{keyword}%')
            )
        # Menggunakan pagination untuk membatasi jumlah twit yang ditampilkan per halaman
        page = request.args.get('page', 1, type=int)
        per_page = 10
        twits_paginated = twits.order_by(Twit.like.desc()).paginate(page, per_page, error_out=False)
        # Memuat hasil pencarian ke dalam objek paginasi
        twits_list = []
        for twit in twits_paginated.items:
            twit_data = {
                'id': twit.public_id,
                'twit': twit.twit_text,
                'username': twit.user_id,
                'date': twit.date_post.strftime('%Y-%m-%d'),
                'likes': twit.likes,
            }
            twits_list.append(twit_data)
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if twits_paginated.has_next:
            next_page = url_for('twits_by_keywords', keywords=keywords, page=twits_paginated.next_num, _external=True)
        return jsonify({'twits': twits_list, 'total_pages': twits_paginated.pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari twit', 'error': str(e)}), 500

# 11. melihat list twit user lain
@app.route('/<username>/twit', methods=['GET'])
def user_twit(username):
    try:
        # Memeriksa apakah author dengan ID yang diberikan ada dalam database
        user = Users.query.get(username)
        if user is None:
            return jsonify({'message': 'User tidak ditemukan'}), 404
        # Mengumpulkan semua quote yang ditulis oleh author dengan ID yang diberikan
        twits = Twit.query.filter_by(username=username).order_by(Twit.date_post.desc()).all()
        return jsonify([
            {
        'id': twit.id,
        'username': twit.username,
        'text': twit.text,
        'date_post': twit.date_post.strftime('%Y-%m-%d %H:%M:%S'),
        'likes': twit.likes,
            } for twit in twits
        ])
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengikut', 'error': str(e)}), 500
    
# 12. Like a Tweet
@app.route('/twit/<public_id>/like', methods=['POST'])
def like_twit(public_id):
    try:
        # Periksa apakah pengguna telah masuk
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum masuk, silakan masuk terlebih dahulu'}), 401
        # Temukan twit berdasarkan public_id
        twit = Twit.query.filter_by(public_id=public_id).first()
        if not twit:
            return jsonify({'message': 'Twit tidak ditemukan'}), 404
        # Tambahkan jumlah like pada twit
        twit.likes += 1
        db.session.commit()
        # Format data twit ke dalam format JSON untuk ditampilkan sebagai respons
        twit_data = {
            'id': twit.public_id,
            'twit': twit.twit_text,
            'username': twit.user_id,
            'date': twit.date.strftime('%Y-%m-%d'),
            'likes': twit.likes,
        }
        return jsonify(twit_data), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat menyukai twit', 'error': str(e)}), 500

