# Import library yang diperlukan dari Flask untuk membuat aplikasi web
from flask import Flask, jsonify, request
# Import library SQLAlchemy untuk bekerja dengan database SQL
# SQLAlchemy adalah pemetaan objek-relasional (ORM). Artinya dengan SQLAlchemy kita tidak perlu menulis perintah SQL mentah. Yang perlu kita lakukan hanyalah membuat model dalam bentuk kelas (objek), dan SQLAlchemy akan melakukan pekerjaan mengubahnya menjadi SQL (database relasional) — oleh karena itu dinamakan pemeta relasional objek.
# Kita dapat melakukan banyak hal dengan ORM - mulai dari melakukan kueri normal hingga menyisipkan, memperbarui, dan menghapus hingga melakukan hal-hal lanjutan seperti menggabungkan, menggabungkan, dll.
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate # menggunakan flask-migrate
# Import library uuid untuk menghasilkan ID unik
import uuid

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi aplikasi Flask. app.config digunakan untuk mengatur konfigurasi aplikasi Flask. Ini adalah objek konfigurasi yang menyimpan berbagai pengaturan untuk aplikasi Flask, seperti kunci rahasia, URI database, dan banyak lagi.
# Dengan menggunakan app.config, kita dapat dengan mudah mengatur berbagai opsi konfigurasi aplikasi Flask tanpa perlu mengubah kode secara langsung. Ini memudahkan pengelolaan dan penyesuaian aplikasi sesuai kebutuhan.
# yang pertama ada secret key, yang digunakan untuk mengamankan aplikasi kita. app.config['SECRET_KEY'] diatur untuk menyimpan kunci rahasia yang digunakan oleh Flask untuk fitur keamanan, seperti pembuatan sesi dan pembuatan token otentikasi.
app.config['SECRET_KEY']='secret'
# Konfigurasi URI database yang digunakan oleh SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] diatur untuk menentukan URI (Uniform Resource Identifier) database yang akan digunakan oleh SQLAlchemy. Dalam kasus ini, itu diatur ke sqlite:///app.db, yang berarti menggunakan SQLite sebagai database dengan file bernama app.db di direktori aplikasi.
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345678@localhost/postgres'

# Inisialisasi objek SQLAlchemy untuk berinteraksi dengan database
# db = SQLAlchemy(app) digunakan untuk membuat instance SQLAlchemy yang terhubung ke aplikasi Flask yang dibuat sebelumnya (app). SQLAlchemy adalah toolkit Python yang sangat kuat untuk bekerja dengan database relasional. Dengan menggunakan SQLAlchemy, kita dapat dengan mudah berinteraksi dengan database dalam aplikasi Flask.
# Secara teknis, ketika kita menggunakan SQLAlchemy dengan aplikasi Flask, SQLAlchemy akan menggunakan objek Flask app untuk mengakses konfigurasi database yang telah diatur, seperti URI database. Ini memungkinkan SQLAlchemy untuk berinteraksi dengan database yang sudah diatur dalam aplikasi Flask dengan mudah dan tanpa harus menuliskan konfigurasi ulang.
db = SQLAlchemy(app)

# migrate = Migrate(app, db)

# Pembuatan model User menggunakan SQLAlchemy
class User(db.Model):
    # Digunakan db.Column untuk membuat kolom.
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(28), nullable=False, unique=True)
    # public_id digunakan sebagai parameter rute karena SQL memberikannya id sebagai bilangan bulat, supaya memiliki nilai UUID yang mirip dengan apa yang kita dapatkan dari ID Mongo.
    public_id = db.Column(db.String, nullable=False)
    # is_admin bidang/kolom, yang akan kita gunakan untuk otorisasi.
    is_admin = db.Column(db.Boolean, default=False)
    # Relasi antara User dan Todo
    # todosfield, yang kami gunakan untuk menghubungkan ke model tugas, sesuai dengan namanya (hubungan). Bagian ini mengambil tiga nilai: Yang pertama mirip dengan yang lain, tergantung pada jenis bidangnya. Yang kedua adalah backref, yang merupakan bidang (variabel) yang kita gunakan untuk mereferensikan model pengguna dalam model tugas. Dan argumen terakhir adalah lazy, yaitu bagaimana data dimuat.
    todos=db.relationship('Todo', backref='owner', lazy='dynamic')

    # Representasi objek User
    # fungsi __repr__ digunakan untuk memberikan deskripsi atau representasi yang dapat dibaca manusia dari objek. Dalam kasus ini, fungsi __repr__ digunakan untuk mengembalikan string yang berisi alamat email pengguna ketika objek User dicetak atau direpresentasikan sebagai string. Misalnya, jika Anda mencetak objek User, Anda akan melihat hasil seperti User <email@contoh.com>. Ini membantu kita memahami objek User dengan lebih baik saat bekerja dengan kode.
    def __repr__(self):
        return f'User <{self.email}>'

# Pembuatan model Todo menggunakan SQLAlchemy
# Ini adalah model tugas
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(20), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    public_id = db.Column(db.String, nullable=False)
    # user_id, yang terakhir adalah kunci asing — yaitu kunci yang digunakan untuk mereferensikan model lain.
    # Dengan kolom ini user_id, saya bisa mendapatkan ID pengguna aplikasi agenda, dan dengan kolom pemilik (dari backref), saya bisa mendapatkan pengguna yang membuat agenda tersebut.
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Representasi objek Todo
    def __repr__(self):
        return f'Todo: <{self.name}>'
   
# matikan jika pakai flask migrate 
with app.app_context():
    db.create_all()
"""
# Pergi ke direktori di mana proyek Flask Anda disimpan
PS D:\Latihan_Bootcamp> cd postgres-latihan

# Memulai interpreter Python
PS D:\Latihan_Bootcamp\postgres-latihan> python
Python 3.12.2...

# Mengimpor instance aplikasi Flask (app) dan instance database (db) dari modul 'alkimia'
>>> from alkimia import app, db

# Menempatkan konteks aplikasi ke dalam app_context, yang memungkinkan kita untuk bekerja dengan aplikasi Flask dalam konteks Shell interaktif
>>> app.app_context().push()

# Membuat semua tabel yang didefinisikan oleh model-model dalam database
>>> db.create_all()

# Mengimpor modul database, model User, dan model Todo
>>> from alkimia import db, User, Todo

# Mencetak instance aplikasi Flask
>>> app
<Flask 'alkimia'>

# Mencetak instance database SQLAlchemy dengan URI database yang ditentukan
>>> db
<SQLAlchemy sqlite:///D:\Latihan_Bootcamp\postgres-latihan\instance\app.db>

# Mencetak class User yang telah dibuat dalam model
>>> User
<class 'alkimia.User'>

# Mencetak class Todo yang telah dibuat dalam model
>>> Todo
<class 'alkimia.Todo'>    

# Melakukan query untuk mendapatkan semua data dari tabel User, yang pada saat ini belum berisi data apa pun
>>> User.query.all() 
[]    

# Melakukan query untuk mendapatkan semua data dari tabel Todo, yang pada saat ini belum berisi data apa pun
>>> Todo.query.all()
[]

# Mengimpor modul uuid untuk membuat public ID yang unik
>>> import uuid 

# Membuat UUID (Universal Unique Identifier) baru sebagai public ID
>>> babs_uid=str(uuid.uuid4())
>>> babs_uid
'42507e28-ae0e-4482-b9bf-0d965bc121f0'

# Membuat instance User baru dengan menggunakan public ID yang telah dibuat
>>> babs=User(
...     name='Babatunde',
...     email='koikibabatunde14@gmail.com',
...     public_id=babs_uid
... )

# Mencetak instance User yang baru dibuat
>>> babs
User <koikibabatunde14@gmail.com>

# Memeriksa apakah ID dari instance User yang baru dibuat adalah None, menunjukkan bahwa baris belum dibuat dalam database
>>> id=babs.id
>>> id
>>> id==None
True

# Menambahkan instance User yang baru dibuat ke dalam sesi database sementara
>>> db.session.add(babs) 

# Melakukan commit untuk menyimpan perubahan secara permanen ke dalam database
>>> db.session.commit() 

# db.session.add_all digunakan untuk mengambil array objek untuk ditambahkan ke database
# db.session.delete untuk menghapus suatu objek.

# Memeriksa kembali ID dari instance User setelah melakukan commit, sekarang ID telah terisi dan bertambah dari 0 menjadi 1
>>> babs.id
1

# Melakukan query untuk mendapatkan semua data dari tabel User, yang sekarang berisi satu baris data
>>> User.query.all()
[User <koikibabatunde14@gmail.com>]       

# Memeriksa apakah instance User yang pertama diambil dari database adalah sama dengan instance User yang baru saja dibuat, menunjukkan bahwa objeknya benar-benar disimpan dalam database
>>> User.query.first()==babs
True

# Mengimpor modul User, Todo, dan db (database) dari modul 'alkimia'
>>> from alkimia import User, Todo, db 

# Mengimpor modul uuid
>>> import uuid

# Membuat UUID baru
>>> id = str(uuid.uuid4())

# Melakukan query untuk mendapatkan instance pertama dari tabel User
>>> u=User.query.first()

# Membuat instance Todo baru dan menghubungkannya dengan instance User yang telah ada
>>> todo=Todo(
... name='Go to market',   
... is_completed=True,
... public_id=id, 
... user_id=u.id
... )

# Mencetak instance Todo yang baru dibuat
>>> todo
Todo: <Go to market>

# Memeriksa user_id dari instance Todo yang baru dibuat
>>> todo.user_id
1

# Menambahkan instance Todo yang baru dibuat ke dalam sesi database sementara
>>> db.session.add(todo)

# Melakukan commit untuk menyimpan perubahan secara permanen ke dalam database
>>> db.session.commit()

# Memeriksa ID dari instance Todo setelah melakukan commit, sekarang ID telah terisi dan bertambah dari 0 menjadi 1
>>> todo.id
1

# Memeriksa pemilik (owner) dari instance Todo yang baru dibuat
>>> todo.owner
User <koikibabatunde14@gmail.com>

# Memeriksa instance User yang digunakan untuk membuat Todo
>>> u
User <koikibabatunde14@gmail.com>

# Melakukan query untuk mendapatkan semua Todo yang dimiliki oleh instance User tersebut
>>> u.todos.all()
[Todo: <Go to market>]
"""

# Routing untuk halaman utama aplikasi
@app.route('/')
def home():
    return {
        'message': 'Selamat datang di pembuatan RESTful APIs dengan Flask dan SQLAlchemy'
    }
    
# Routing untuk mendapatkan semua pengguna
@app.route('/users/')
def get_users():
    return jsonify([
        {
            'id': user.public_id, 'name': user.name, 'email': user.email,
            'is admin': user.is_admin
            } for user in User.query.all()
    ])

# Routing untuk mendapatkan pengguna berdasarkan ID
@app.route('/users/<id>/')
def get_user(id):
    # Dalam get_usersfungsinya, kami mengembalikan array pengguna. Daripada mengembalikan id, kami mengembalikan public_id, yang digunakan sebagai parameter rute. 
    # Kode status defaultnya adalah 200, jadi kita tidak perlu meneruskannya di sini. Mari kita uji titik akhir ini sekarang.
    user = User.query.filter_by(public_id=id).first_or_404()
    return {
        'id': user.public_id, 'name': user.name, 
        'email': user.email, 'is admin': user.is_admin
    }

# Titik akhir untuk kedua fungsi ini diberikan di app.routedekorator. Jika kita mengembalikan kamus, Flask secara otomatis mengubahnya menjadi JSON, itulah sebabnya kita tidak menggunakan fungsi jsonifydi fungsi kedua.

# Routing untuk membuat pengguna baru
@app.route('/users/', methods=['POST'])
def create_user():
    # Fungsi ini POST menerima sedikit data JSON
    data = request.get_json()
    # Validasi data yang diterima
    # Pertama-tama verifikasi nama dan email yang diberikan dan panjangnya setidaknya empat karakter 
    if not 'name' in data or not 'email' in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Name or email not given'
        }), 400
    if len(data['name']) < 4 or len(data['email']) < 6:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Name and email must be contain minimum of 4 letters'
        }), 400
    # Membuat objek User baru dan menyimpannya ke database
    u = User(
            name=data['name'], 
            email=data['email'],
            is_admin=data.get('is admin', False),
            public_id=str(uuid.uuid4())
        )
    db.session.add(u)
    db.session.commit()
    # Memberikan respons dengan data pengguna yang baru dibuat
    # Kami mengembalikan data JSON pengguna dan kode status 201 untuk CREATED.
    return {
        'id': u.public_id, 'name': u.name, 
        'email': u.email, 'is admin': u.is_admin 
    }, 201

# Routing untuk memperbarui data pengguna berdasarkan ID
@app.route('/users/<id>/', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    # data JSON untuk apa yang ingin kami perbarui — dalam hal ini, harus berupa name.
    if 'name' not in data:
        return {
            'error': 'Bad Request',
            'message': 'Name field needs to be present'
        }, 400
    #  Kami pertama kali mendapatkan pengguna dengan ID publik di parameter rute.
    user = User.query.filter_by(public_id=id).first_or_404()
    # Memperbarui data pengguna
    # Kemudian, kami memperbarui bidang tersebut dan memanggil db.session.commit()
    user.name=data['name']
    if 'is admin' in data:
        user.is_admin=data['admin']
    db.session.commit()
    # Memberikan respons dengan data pengguna yang diperbarui
    # Kami akhirnya mengembalikan data pengguna yang diperbarui dengan kode status 200 (default)
    return jsonify({
        'id': user.public_id, 
        'name': user.name, 'is admin': user.is_admin,
        'email': user.email
    })

# Routing untuk menghapus pengguna berdasarkan ID
@app.route('/users/<id>/', methods=['DELETE'] )
def delete_user(id):
    # Kedua fungsi ini menggunakan first_or_404 fungsi dalam memfilter data — sehingga kesalahan 404 akan ditampilkan jika tidak ada pengguna yang memiliki ID publik tersebut di URL.
    user = User.query.filter_by(public_id=id).first_or_404()
    # Menghapus pengguna dari database
    db.session.delete(user)
    db.session.commit()
    # Memberikan respons sukses
    return {
        'success': 'Data deleted successfully'
    }

# Sekarang mari kita mulai dengan todo endpoint.
# Routing untuk mendapatkan semua tugas
@app.route('/todos/')
def get_todos():
    return jsonify([
        { 
            'id': todo.public_id, 'name': todo.name,
            'owner': {
                'name': todo.owner.name,
                'email': todo.owner.email,
                'public_id': todo.owner.public_id
            }
        } for todo in Todo.query.all()
    ])

# Routing untuk mendapatkan tugas berdasarkan ID
@app.route('/todos/<id>')
def get_todo(id):
    todo = Todo.query.filter_by(public_id=id).first_or_404()
    # Memberikan respons dengan data tugas
    return jsonify({ 
            'id': todo.public_id, 'name': todo.name,
            'owner': {
                'name': todo.owner.name,
                'email': todo.owner.email,
                'public_id': todo.owner.public_id
            }
        })

# Routing untuk membuat tugas baru
@app.route('/todos/', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not 'name' in data or not 'email' in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Name of todo or email of creator not given'
        }), 400
    if len(data['name']) < 4:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Name of todo contain minimum of 4 letters'
        }),
        400

    # Mengambil pengguna berdasarkan email yang diberikan dalam data
    # Kita dapat menggunakan public_idor email untuk mendapatkan objek pengguna karena kedua bidang ini unik. Saya rasa saya akan menggunakan email karena mudah diingat. Jadi saat membuat yang baru todo, kita harus meneruskan email pembuatnya juga.
    user=User.query.filter_by(email=data['email']).first()
    if not user:
        return {
            'error': 'Bad request',
            'message': 'Invalid email, no user with that email'
        }
    # Mengambil status is_completed dari data atau mengatur defaultnya menjadi False
    is_completed = data.get('is completed', False)
    # Membuat objek Todo baru dan menyimpannya ke database
    todo = Todo(
        name=data['name'], user_id=user.id,
        is_completed=is_completed, public_id=str(uuid.uuid4())
    )
    db.session.add(todo)
    db.session.commit()
    # Memberikan respons dengan data tugas yang baru dibuat
    return {
        'id': todo.public_id, 'name': todo.name, 
        'completed': todo.is_completed,
        'owner': {
            'name': todo.owner.name,
            'email': todo.owner.email,
            'is admin': todo.owner.is_admin 
        } 
    }, 201

# Routing untuk memperbarui tugas berdasarkan ID
@app.route('/todos/<id>/', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    # Memeriksa apakah data nama atau status completed diberikan
    if not 'name' in data or not 'completed' in data:
        return {
            'error': 'Bad Request',
            'message': 'Name or completed fields need to be present'
        }, 400
    todo = Todo.query.filter_by(public_id=id).first_or_404()
    # Memperbarui data tugas
    todo.name=data.get('name', todo.name)
    if 'completed' in data:
        todo.completed=data['completed']
    db.session.commit()
    # Memberikan respons dengan data tugas yang diperbarui
    return {
        'id': todo.public_id, 'name': todo.name, 
        'completed': todo.completed,
        'owner': {
            'name': todo.owner.name, 'email': todo.owner.email,
            'is admin': todo.owner.is_admin 
        } 
    }, 201

# Routing untuk menghapus tugas berdasarkan ID
@app.route('/todos/<id>/', methods=['DELETE'] )
def delete_todo(id):
    todo = Todo.query.filter_by(public_id=id).first_or_404()
    # Menghapus tugas dari database
    db.session.delete(todo)
    db.session.commit()
    # Memberikan respons sukses
    return {
        'success': 'Data deleted successfully'
    }

# Menjalankan aplikasi Flask jika dijalankan sebagai script utama
if __name__ == '__main__':
    app.run(debug=True)
