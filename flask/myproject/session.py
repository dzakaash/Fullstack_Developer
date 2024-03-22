from flask import session, request, redirect, url_for, Flask

# Import objek-session dari modul flask untuk mengelola sesi pengguna.

app = Flask(__name__)

# Tetapkan kunci rahasia yang digunakan untuk mengamankan data sesi pengguna.
# Kunci rahasia ini harus dijaga kerahasiaannya agar keamanan sesi tetap terjamin.
# Gunakan perintah di bawah untuk menghasilkan kunci rahasia secara acak.
# $ python -c 'import secrets; print(secrets.token_hex())'
# Pastikan untuk menggantikan nilai 'b'_5#y2L"F4Q8z\n\xec]/'' dengan kunci rahasia yang dihasilkan.

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Dilog masuk sebagai {session["username"]}'
    return 'Anda belum masuk'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Jika metode permintaan adalah POST, simpan nama pengguna dalam sesi.
        session['username'] = request.form['username']
        # Setelah menyimpan nama pengguna, redirect ke halaman utama.
        return redirect(url_for('index'))
    # Jika metode permintaan adalah GET, tampilkan formulir login.
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # Hapus data sesi 'username' jika ada.
    session.pop('username', None)
    # Setelah logout, redirect kembali ke halaman utama.
    return redirect(url_for('index'))

# Penggunaan objek-session memungkinkan aplikasi untuk menyimpan data sesi pengguna di server.
# Data ini akan dienkripsi sebelum disimpan dalam cookie pengguna.
# Pastikan untuk menjaga kunci rahasia (secret_key) agar tidak bocor.

# Untuk menggunakan sesi dalam Flask, Anda perlu memastikan bahwa kunci rahasia (secret_key) ditetapkan untuk aplikasi Anda.
# Anda dapat menghasilkan kunci rahasia secara acak menggunakan perintah yang disediakan di atas.

# Setelah menjalankan aplikasi, buka browser dan kunjungi alamat yang sesuai untuk mengakses aplikasi Flask.

# Jika Anda ingin menangani sesi di sisi server, ada beberapa ekstensi Flask yang mendukung ini.

# Instruksi di bawah ini akan menjalankan aplikasi Flask secara lokal.
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
