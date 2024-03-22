# Pertama, kita mengimpor kelas Flask dari pustaka Flask.
from flask import Flask, render_template

# Kemudian, kita membuat sebuah instance dari kelas Flask tersebut dengan menyediakan nama modul atau paket aplikasi kita sebagai argumen pertama. 'name' adalah cara singkat yang nyaman untuk menentukan hal tersebut yang umumnya sesuai untuk kebanyakan kasus. Hal ini diperlukan agar Flask tahu di mana mencari sumber daya seperti template dan file statis.
app = Flask(__name__)

# Selanjutnya, kita menggunakan decorator route() untuk memberi tahu Flask URL mana yang akan memicu fungsi kita.
@app.route("/")
# Fungsi tersebut mengembalikan pesan yang ingin kita tampilkan di browser pengguna. Tipe konten defaultnya adalah HTML, sehingga HTML dalam string tersebut akan dirender oleh browser.
def hello_world():
    return "<p>Hello, World!</p>"
    # Jika ingin merender template HTML dari file, gunakan kode berikut:
    # return render_template('index.html')

# Routing (Pengarahan) adalah cara di mana aplikasi web menentukan bagaimana menanggapi permintaan yang masuk ke berbagai URL. Aplikasi web modern menggunakan URL yang bermakna untuk membantu pengguna. Pengguna cenderung lebih menyukai halaman dan kembali jika halaman tersebut menggunakan URL yang bermakna yang dapat mereka ingat dan gunakan untuk mengunjungi halaman secara langsung.
# Anda dapat menggunakan decorator route() untuk menghubungkan sebuah fungsi dengan sebuah URL.
# Contoh penambahan fungsi routing:
@app.route('/indeks')
def index():
    return 'Halaman Indeks'

@app.route('/hello')
def hello():
    return 'Halo, Dunia!'

# URL kanonikal untuk titik akhir proyek memiliki garis miring di akhir. Ini mirip dengan sebuah folder dalam sistem file. Jika Anda mengakses URL tanpa garis miring di akhir (/projects), Flask akan mengalihkan Anda ke URL kanonikal dengan garis miring di akhir (/projects/).
# URL kanonikal untuk titik akhir tentang tidak memiliki garis miring di akhir. Ini mirip dengan jalur file dari sebuah file. Mengakses URL dengan garis miring di akhir (/about/) akan menghasilkan kesalahan 404 "Tidak Ditemukan". Ini membantu menjaga URL menjadi unik untuk sumber daya tersebut, yang membantu mesin pencari menghindari pengindeksan halaman yang sama dua kali.
@app.route('/projects/')
def projects():
    return 'Halaman proyek'

@app.route('/about')
def about():
    return 'Halaman tentang'

# Uncomment kode di bawah untuk menjalankan aplikasi Flask secara lokal.
if __name__ == '__main__':
    app.run(debug=True)

# Untuk menjalankan aplikasi Flask:
# 1. Pastikan Anda memiliki Flask terinstal di lingkungan Python Anda.
# 2. Simpan skrip ini dengan nama file app.py.
# 3. Buka terminal atau command prompt, lalu arahkan ke direktori tempat file app.py disimpan.
# 4. Jalankan perintah `python app.py`.
# 5. Buka browser dan kunjungi alamat http://127.0.0.1:5000/ untuk melihat hasilnya.
