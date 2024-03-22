from flask import Flask, request
from werkzeug.utils import secure_filename

# Import Flask dan request untuk mengelola unggahan file, serta secure_filename untuk menjamin keamanan nama file.

app = Flask(__name__)

@app.route('/unggah', methods=['GET', 'POST'])
def unggah_file():
    if request.method == 'POST':
        # Dapatkan objek file yang diunggah dari permintaan.
        file = request.files['the_file']
        # Simpan file tersebut di lokasi yang ditentukan di sistem file server.
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")

# Fungsi di atas adalah contoh sederhana bagaimana mengelola unggahan file menggunakan Flask.
# Pertama, pastikan bahwa formulir HTML Anda memiliki atribut enctype="multipart/form-data" agar browser dapat mengirimkan file.
# Kemudian, pada rute '/unggah', cek apakah metode permintaan adalah POST (artinya, file sedang diunggah).
# Dapatkan objek file yang diunggah dari permintaan dengan menggunakan request.files['nama_kunci'].
# Simpan file tersebut di lokasi yang diinginkan di sistem file server dengan menggunakan metode save().

# Jika Anda ingin mengetahui nama file di sisi klien sebelum diunggah ke aplikasi Anda, Anda dapat mengakses atribut filename.
# Namun, pastikan untuk tidak mempercayai nilai tersebut sepenuhnya karena dapat dipalsukan.
# Untuk memastikan keamanan, lewatkan nama file tersebut melalui fungsi secure_filename() sebelum menyimpannya.

# Untuk menggunakan aplikasi Flask, pastikan Anda memiliki modul yang diperlukan seperti Flask dan Werkzeug.
# Setelah itu, jalankan aplikasi menggunakan perintah app.run() seperti yang tertera di bawah.

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
