from flask import Flask, url_for
# Import Flask untuk membuat aplikasi web dan url_for untuk menghasilkan URL untuk gambar pengguna.

app = Flask(__name__)

@app.route("/saya")
def api_saya():
    # Fungsi ini menangani permintaan ke endpoint '/saya' dan mengembalikan data pengguna dalam format JSON.
    # Pengguna saat ini diambil dengan menggunakan fungsi dapatkan_pengguna_saat_ini().
    # Data pengguna, seperti username, theme, dan image, dikembalikan dalam bentuk dictionary.
    # URL gambar pengguna dihasilkan menggunakan url_for dengan mengambil nama fungsi gambar_pengguna dan nama file gambar pengguna.
    pengguna = dapatkan_pengguna_saat_ini()
    return {
        "username": pengguna.username,
        "theme": pengguna.theme,
        "image": url_for("gambar_pengguna", filename=pengguna.gambar),
    }

@app.route("/pengguna")
def api_pengguna():
    # Fungsi ini menangani permintaan ke endpoint '/pengguna' dan mengembalikan daftar pengguna dalam format JSON.
    # Semua pengguna diambil dengan menggunakan fungsi dapatkan_semua_pengguna().
    # Setiap objek pengguna diubah menjadi format JSON menggunakan metode ke_json().
    pengguna = dapatkan_semua_pengguna()
    return [pengguna.ke_json() for pengguna in pengguna]

# Kode di atas mengatur dua endpoint: '/saya' untuk mengambil data pengguna saat ini dan '/pengguna' untuk mengambil daftar semua pengguna.

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
