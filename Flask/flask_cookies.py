from flask import Flask, request, make_response, render_template
# Import Flask, request, dan make_response untuk mengelola cookies.

app = Flask(__name__)

@app.route('/')
def index():
    # Fungsi ini menangani permintaan ke endpoint '/'.
    # Di sini, kita membaca cookie 'username' dari permintaan menggunakan request.cookies.get().
    # Menggunakan cookies.get(key) daripada cookies[key] akan mencegah KeyError jika cookie tidak ada.
    username = request.cookies.get('username')
    # Setelah mendapatkan nilai cookie 'username', Anda dapat menggunakannya sesuai kebutuhan.
    # Misalnya, Anda dapat menggunakan nilai tersebut untuk menampilkan pesan selamat datang kepada pengguna.

# Menyimpan cookies:
@app.route('/')
def index():
    # Fungsi ini menangani permintaan ke endpoint '/'.
    # Di sini, kita membuat respons menggunakan make_response() yang mencakup render_template().
    resp = make_response(render_template(...))
    # Kemudian, kita menggunakan resp.set_cookie() untuk menetapkan cookie dengan nama 'username' dan nilai 'nama pengguna'.
    resp.set_cookie('username', 'nama pengguna')
    # Kemudian, respons yang telah dimodifikasi dengan cookie ditampilkan.
    return resp
    # Perhatikan bahwa cookies diatur pada objek respons, bukan pada objek permintaan.

# Instruksi menjalankan aplikasi Flask akan ditambahkan di akhir kode.

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
