from markupsafe import escape
from flask import Flask

app = Flask(__name__)

# Saat mengembalikan HTML (tipe respons default dalam Flask), semua nilai yang diberikan oleh pengguna yang dirender dalam output harus di-escape untuk melindungi dari serangan injeksi. Template HTML yang dirender dengan Jinja, yang akan dijelaskan nanti, akan melakukan ini secara otomatis.

# escape(), yang ditunjukkan di sini, dapat digunakan secara manual. Hal ini tidak disertakan dalam sebagian besar contoh untuk kekompakan, tetapi Anda harus selalu menyadari bagaimana Anda menggunakan data yang tidak dapat dipercaya
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

# Anda dapat menambahkan bagian variabel ke sebuah URL dengan menandai bagian-bagian tersebut dengan <nama_variabel>. Fungsi Anda kemudian menerima <nama_variabel> sebagai argumen kata kunci. Opsionalnya, Anda dapat menggunakan konverter untuk menentukan jenis argumen seperti konverter:nama_variabel.
# Tipe-tipe konverter:
# - string (default): menerima teks apa pun tanpa garis miring
# - int: menerima bilangan bulat positif
# - float: menerima nilai floating point positif
# - path: seperti string tetapi juga menerima garis miring
# - uuid: menerima string UUID
@app.route('/user/<username>')
def show_user_profile(username):
    # menampilkan profil pengguna untuk pengguna tersebut
    return f'Profil Pengguna {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # menampilkan pos dengan id yang diberikan, id tersebut adalah integer
    return f'Pos {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # menampilkan subpath setelah /path/
    return f'Subpath {escape(subpath)}'

# Uncomment kode di bawah untuk menjalankan aplikasi Flask secara lokal.
if __name__ == '__main__':
    app.run(debug=True)

# Untuk menjalankan aplikasi Flask:
# 1. Pastikan Anda memiliki Flask terinstal di lingkungan Python Anda.
# 2. Simpan skrip ini dengan nama file app.py.
# 3. Buka terminal atau command prompt, lalu arahkan ke direktori tempat file app.py disimpan.
# 4. Jalankan perintah `python app.py`.
# 5. Buka browser dan kunjungi alamat http://127.0.0.1:5000/ untuk melihat hasilnya.
