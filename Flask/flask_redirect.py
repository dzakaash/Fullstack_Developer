from flask import abort, redirect, url_for
from flask import Flask

app = Flask(__name__)

# Untuk mengalihkan pengguna ke endpoint lain, gunakan fungsi redirect(); untuk membatalkan permintaan dengan kode kesalahan, gunakan fungsi abort():
@app.route('/')
def index():
    return redirect(url_for('login')) # Mengalihkan pengguna ke halaman login

@app.route('/login')
def login():
    abort(401) # Membatalkan permintaan dengan kode kesalahan 401 (Akses Ditolak)
    this_is_never_executed() # Kode di bawah fungsi abort() tidak akan pernah dieksekusi

# Ini adalah contoh yang agak tidak berguna karena pengguna akan diarahkan dari indeks ke halaman yang tidak dapat diakses (401 berarti akses ditolak) tetapi itu menunjukkan bagaimana cara kerjanya.
# Secara default, halaman kesalahan hitam putih ditampilkan untuk setiap kode kesalahan. Jika Anda ingin menyesuaikan halaman kesalahan, Anda dapat menggunakan decorator errorhandler():
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
# Perhatikan angka 404 setelah panggilan render_template(). Ini memberi tahu Flask bahwa kode status halaman tersebut harus 404 yang berarti tidak ditemukan. Secara default, diasumsikan 200 yang diterjemahkan menjadi: semuanya berjalan dengan baik.
# Lihat Penanganan Kesalahan Aplikasi untuk lebih detailnya.

# Nilai kembalian dari sebuah fungsi tampilan secara otomatis dikonversi menjadi objek respons untuk Anda. Jika nilai kembalian berupa string, itu dikonversi menjadi objek respons dengan string sebagai isi respons, kode status 200 OK, dan tipe konten text/html. Jika nilai kembalian berupa dict atau list, jsonify() dipanggil untuk menghasilkan respons. Logika yang diterapkan Flask untuk mengonversi nilai kembalian menjadi objek respons adalah sebagai berikut:
# Jika objek respons dari jenis yang benar dikembalikan, itu langsung dikembalikan dari tampilan.
# Jika itu adalah string, objek respons dibuat dengan data tersebut dan parameter default.
# Jika itu adalah iterator atau generator yang mengembalikan string atau bytes, itu dianggap sebagai respons streaming.
# Jika itu adalah dict atau list, objek respons dibuat menggunakan jsonify().
# Jika sebuah tuple dikembalikan, item dalam tuple tersebut dapat memberikan informasi tambahan. Tuple-tuple tersebut harus dalam bentuk (respons, status), (respons, headers), atau (respons, status, headers). Nilai status akan mengganti kode status dan headers dapat berupa daftar atau kamus dari nilai header tambahan.
# Jika tidak ada yang cocok, Flask akan menganggap nilai kembalian adalah aplikasi WSGI yang valid dan mengonversinya menjadi objek respons.
# Jika Anda ingin mendapatkan objek respons yang dihasilkan di dalam tampilan, Anda dapat menggunakan fungsi make_response().

# Bayangkan Anda memiliki tampilan seperti ini:
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

# Anda hanya perlu melingkupi ekspresi pengembalian dengan make_response() dan mendapatkan objek respons untuk memodifikasinya, lalu mengembalikannya:
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'Sebuah nilai'
    return resp

# Uncomment kode di bawah untuk menjalankan aplikasi Flask secara lokal.
# if __name__ == '__main__':
#     app.run(debug=True)

# Untuk menjalankan aplikasi Flask:
# 1. Pastikan Anda memiliki Flask terinstal di lingkungan Python Anda.
# 2. Simpan skrip ini dengan nama file app.py.
# 3. Buka terminal atau command prompt, lalu arahkan ke direktori tempat file app.py disimpan.
# 4. Jalankan perintah `python app.py`.
# 5. Buka browser dan kunjungi alamat http://127.0.0.1:5000/ untuk melihat hasilnya.
