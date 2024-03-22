from flask import request, render_template, Flask

# Flask memungkinkan aplikasi web untuk bereaksi terhadap data yang dikirim oleh klien ke server melalui objek request global.
# Objek request global menyediakan informasi yang diperlukan untuk mengakses data yang dikirim dalam permintaan HTTP.

app = Flask(__name__)

# Contoh penggunaan objek request dalam Flask:
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Username/kata sandi tidak valid'
    # Jika metode permintaan adalah GET atau kredensial tidak valid, halaman login akan dirender dengan pesan kesalahan (jika ada).
    return render_template('login.html', error=error)

# Saat menggunakan form dalam template HTML, data formulir yang dikirim dalam permintaan POST atau PUT dapat diakses melalui atribut form.
# Penggunaan atribut form:
# request.form['nama_kunci'] -> Mengakses nilai yang dikirimkan dengan kunci tertentu dalam data form.
# Perhatian: Jika kunci tidak ada dalam form, akan terjadi KeyError.

# Untuk mengakses parameter yang dikirimkan dalam URL (?key=value), gunakan atribut args.
# Penggunaan atribut args:
# request.args.get('key', '') -> Mendapatkan nilai parameter yang dikirim dalam URL dengan kunci tertentu.
# Jika kunci tidak ditemukan, nilai default (dalam contoh ini, string kosong) akan digunakan.

# Berikut adalah contoh penggunaan objek request untuk menangani permintaan HTTP:
searchword = request.args.get('key', '')

# Setelah mengakses data dari permintaan, Anda dapat melakukan operasi logika dan pengolahan data sesuai kebutuhan aplikasi.

# Setelah menyelesaikan logika pengolahan data, biasanya Anda akan memberikan respons kepada pengguna.
# Respons dapat berupa halaman HTML yang dirender menggunakan template atau data JSON, tergantung pada kebutuhan aplikasi.

# Untuk menjalankan aplikasi Flask:
if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port=5000)
