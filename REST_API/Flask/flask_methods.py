from flask import request
from flask import Flask

app = Flask(__name__)

# Saat mengakses URL, aplikasi web menggunakan metode HTTP yang berbeda, seperti GET atau POST. Penting untuk memahami perbedaan antara metode HTTP saat bekerja dengan Flask. Secara default, sebuah rute hanya menanggapi permintaan GET. Namun, Anda dapat menggunakan argumen 'methods' dari decorator route() untuk menangani metode HTTP yang berbeda.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'lakukan_login()' # Panggil fungsi lakukan_login() jika permintaan adalah POST
    else:
        return 'tampilkan_form_login()' # Tampilkan form login jika permintaan adalah GET

# Contoh di atas menjaga semua metode untuk rute tersebut dalam satu fungsi, yang dapat berguna jika setiap bagian menggunakan beberapa data yang umum.
# Anda juga dapat memisahkan tampilan untuk metode yang berbeda ke dalam fungsi yang berbeda. Flask menyediakan pintasan untuk mendekorasi rute-rute tersebut dengan get(), post(), dll. untuk setiap metode HTTP umum.
# @app.get('/login')
# def login_get():
#     return 'tampilkan_form_login()' # Tampilkan form login jika permintaan adalah GET

# @app.post('/login')
# def login_post():
#     return 'lakukan_login()' # Panggil fungsi lakukan_login() jika permintaan adalah POST

# Jika metode GET hadir, Flask secara otomatis menambahkan dukungan untuk metode HEAD dan menangani permintaan HEAD sesuai dengan RFC HTTP. Demikian pula, OPTIONS secara otomatis diimplementasikan untuk Anda.

# Uncomment kode di bawah untuk menjalankan aplikasi Flask secara lokal.
if __name__ == '__main__':
    app.run(debug=True)

# Untuk menjalankan aplikasi Flask:
# 1. Pastikan Anda memiliki Flask terinstal di lingkungan Python Anda.
# 2. Simpan skrip ini dengan nama file app.py.
# 3. Buka terminal atau command prompt, lalu arahkan ke direktori tempat file app.py disimpan.
# 4. Jalankan perintah `python app.py`.
# 5. Buka browser dan kunjungi alamat http://127.0.0.1:5000/ untuk melihat hasilnya.
