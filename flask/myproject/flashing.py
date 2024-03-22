from flask import Flask, flash, redirect, render_template, request, url_for
# Import Flask dan modul-modul lain yang diperlukan.

app = Flask(__name__)
# Inisialisasi aplikasi Flask.

# Pesan Flashing
# Sistem flashing pada Flask memungkinkan Anda untuk memberikan umpan balik kepada pengguna dengan cara yang sederhana.
# Metode flash() digunakan untuk menyimpan pesan yang akan ditampilkan kepada pengguna pada permintaan berikutnya.
# Metode get_flashed_messages() digunakan untuk mendapatkan pesan-pesan yang telah disimpan dan menampilkannya kepada pengguna.
# Pesan-pesan flashing biasanya digunakan untuk memberi tahu pengguna tentang kejadian atau informasi penting setelah sebuah tindakan tertentu.
# Contoh penggunaan pesan flashing:
@app.route('/')
def index():
    flash('Selamat datang!')
    return render_template('index.html')

# Logging
# Flask menyediakan logger yang siap digunakan untuk mencatat informasi, peringatan, atau kesalahan.
# Anda dapat menggunakan metode logger.debug(), logger.warning(), atau logger.error() untuk mencatat pesan-pesan sesuai dengan tingkat kepentingan.
# Contoh penggunaan logger:
@app.route('/log')
def log():
    app.logger.debug('Sebuah nilai untuk debugging')
    app.logger.warning('Terjadi peringatan (%d apel)', 42)
    app.logger.error('Terjadi kesalahan')
    return 'Log telah dicatat.'

# Middleware WSGI
# Anda dapat menambahkan middleware WSGI ke aplikasi Flask dengan membungkus atribut wsgi_app aplikasi.
# Middleware ini berguna untuk memodifikasi permintaan atau respons sebelum atau sesudah mereka mencapai aplikasi Flask Anda.
# Contoh penggunaan middleware ProxyFix:
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

# Menggunakan Ekstensi Flask
# Flask menyediakan berbagai ekstensi yang membantu dalam menyelesaikan tugas-tugas umum.
# Contoh ekstensi yang populer adalah Flask-SQLAlchemy yang menyediakan integrasi dengan SQLAlchemy untuk pengelolaan basis data.
# Untuk menggunakan ekstensi, Anda perlu menginstalnya terlebih dahulu menggunakan pip, kemudian mengimpor dan mendaftarkannya ke aplikasi Flask Anda.
# Contoh penggunaan Flask-SQLAlchemy:
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

# Implementasi ke Server Web
# Setelah Anda selesai mengembangkan aplikasi Flask Anda, Anda dapat mengimplementasikannya ke server web menggunakan panduan Implementasi ke Produksi.
# Panduan tersebut akan membantu Anda dalam menjalankan aplikasi Flask Anda secara aman dan efisien di lingkungan produksi.

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
