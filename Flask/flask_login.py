from flask import url_for
from flask import Flask

# Fungsi url_for() digunakan untuk membangun URL ke fungsi tertentu. Fungsi ini menerima nama fungsi sebagai argumen pertamanya dan sejumlah argumen kata kunci, masing-masing sesuai dengan bagian variabel aturan URL. Bagian variabel yang tidak dikenal akan ditambahkan ke URL sebagai parameter query.

# Fungsi url_for() sangat berguna karena:
# 1. Lebih deskriptif daripada menuliskan URL secara manual.
# 2. Mengubah URL bisa dilakukan secara keseluruhan tanpa perlu mengingat untuk mengubahnya secara manual.
# 3. Mengatasi penghindaran karakter khusus secara transparan.
# 4. URL yang dihasilkan selalu absolut, menghindari perilaku tak terduga dari jalur relatif di browser.
# 5. Menangani penempatan aplikasi di luar akar URL dengan benar.

# Sebagai contoh, di bawah ini kami menggunakan metode test_request_context() untuk mencoba url_for(). test_request_context() memberi tahu Flask untuk bertindak seolah-olah sedang menangani sebuah permintaan bahkan saat kita menggunakan shell Python. Lihat Context Locals.

app = Flask(__name__)

@app.route('/')
def index():
    return 'indeks'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'Profil {username}'

with app.test_request_context():
    print(url_for('index')) # Menghasilkan URL untuk fungsi index
    print(url_for('login')) # Menghasilkan URL untuk fungsi login
    print(url_for('login', next='/')) # Menambahkan parameter query 'next' ke URL untuk fungsi login
    print(url_for('profile', username='John Doe')) # Menghasilkan URL untuk fungsi profile dengan argumen username='John Doe'
    
    # Aplikasi web dinamis juga memerlukan file statis. Biasanya di situlah file CSS dan JavaScript berasal. Idealnya, server web Anda dikonfigurasi untuk melayani file-file tersebut, tetapi selama pengembangan Flask juga dapat melakukannya. Cukup buat folder bernama static di paket Anda atau di sebelah modul Anda, dan folder tersebut akan tersedia di /static pada aplikasi.
    # Untuk menghasilkan URL untuk file-file statis, gunakan nama endpoint 'static' yang khusus. File harus disimpan di sistem berkas sebagai static/style.css:
    # url_for('static', filename='style.css')

# Uncomment kode di bawah untuk menjalankan aplikasi Flask secara lokal.
if __name__ == '__main__':
    app.run(debug=True)

# Untuk menjalankan aplikasi Flask:
# 1. Pastikan Anda memiliki Flask terinstal di lingkungan Python Anda.
# 2. Simpan skrip ini dengan nama file app.py.
# 3. Buka terminal atau command prompt, lalu arahkan ke direktori tempat file app.py disimpan.
# 4. Jalankan perintah `python app.py`.
# 5. Buka browser dan kunjungi alamat http://127.0.0.1:5000/ untuk melihat hasilnya.
