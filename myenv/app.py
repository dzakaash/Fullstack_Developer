from flask import Flask, render_template
# from flask import Flask, render_template: Mengimpor Flask dan fungsi render_template dari modul Flask. 
# Flask adalah sebuah framework web untuk Python yang memungkinkan kita untuk membuat aplikasi web dengan mudah. 
# Fungsi render_template digunakan untuk merender template HTML.

# Membuat instance Flask dengan nama aplikasi yang sama dengan nama file ini.
# Ini berarti aplikasi akan menangani permintaan HTTP ke URL utama atau root.
app = Flask(__name__)

# Mendefinisikan route '/' yang merupakan titik akhir dari aplikasi web Flask.
@app.route('/')
def index():
    # Fungsi index() akan dipanggil ketika ada permintaan ke route '/'.
    # Fungsi ini merender (menampilkan) template 'index.html' sebagai halaman utama.
    return render_template('index.html')

# Memastikan bahwa aplikasi hanya dijalankan jika file ini dijalankan langsung 
# (bukan diimpor ke dalam file lain).
if __name__ == "__main__":
    # Mengaktifkan mode debug untuk memudahkan pemecahan masalah saat pengembangan.
    # Ini akan menjalankan server Flask secara lokal sehingga aplikasi dapat diakses 
    # melalui browser dengan alamat http://localhost:5000/.
    app.run(debug=True)
