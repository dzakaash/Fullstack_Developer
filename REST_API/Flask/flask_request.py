
from flask import Flask, request, jsonify, render_template, make_response
app = Flask(__name__)
# 1. Get Parameter
@app.route('/halo')
def halo():
    # Mendapatkan nilai parameter 'name' dari URL menggunakan request.args.get()
    name = request.args.get('name')
    
    if name:
        # Jika parameter 'name' ada, maka mengembalikan pesan salam dengan nama yang diberikan
        return f'Halo, {name}!'
    else:
        # Jika parameter 'name' tidak ada, mengembalikan pesan default
        return 'Halo, pengunjung!'

# 2. Post Parameter
@app.route('/login', methods=['POST'])
def login():
    # Mendapatkan nilai parameter 'username' dari body permintaan POST menggunakan request.form.get()
    username = request.form.get('username')
    
    # Mendapatkan nilai parameter 'password' dari body permintaan POST menggunakan request.form.get()
    password = request.form.get('password')
    
    # Memeriksa apakah kedua parameter telah diberikan
    if username and password:
        # Jika kedua parameter diberikan, melakukan proses autentikasi
        if username == 'user' and password == 'pass':
            return 'Login berhasil!'
        else:
            return 'Kombinasi username dan password salah!'
    else:
        # Jika salah satu atau kedua parameter tidak diberikan, mengembalikan pesan error
        return 'Harap masukkan username dan password.'

# 3. Path Parameter
@app.route('/hello/<nama>')
def hello(nama):
    # Fungsi ini akan menerima nilai parameter 'nama' dari URL
    # Nilai 'nama' akan diambil dari bagian path URL yang sesuai dengan <nama>
    # Misalnya, jika URL adalah '/hello/Alice', maka nilai 'nama' akan menjadi 'Alice'
    
    # Mengembalikan pesan salam dengan nama yang diberikan
    return f'Halo, {nama}!'

# 4. JSON Parameter
@app.route('/data', methods=['POST'])
def process_data():
    # Mendapatkan data JSON dari body permintaan menggunakan request.json
    data = request.json
    
    # Memeriksa apakah data berhasil diterima
    if data:
        # Jika data diterima, mengakses nilai 'nama' dari JSON
        nama = data.get('nama')
        
        # Jika 'nama' ada dalam data, mengembalikan pesan salam
        if nama:
            return jsonify({'pesan': f'Halo, {nama}!'})
        else:
            # Jika 'nama' tidak ada dalam data, mengembalikan pesan error
            return jsonify({'pesan': 'Nama tidak ditemukan dalam data JSON.'}), 400
    else:
        # Jika tidak ada data JSON yang diterima, mengembalikan pesan error
        return jsonify({'pesan': 'Data JSON tidak ditemukan dalam permintaan.'}), 400

# 5. Header Parameter
@app.route('/header')
def process_header():
    # Mendapatkan nilai header 'User-Agent' menggunakan request.headers.get()
    user_agent = request.headers.get('User-Agent')
    
    # Mendapatkan nilai header 'Content-Type' menggunakan request.headers.get()
    content_type = request.headers.get('Content-Type')
    
    pemilik = request.headers.get("Pemilik")
    
    # Menyiapkan pesan yang akan ditampilkan
    pesan = f'Nilai header User-Agent: {user_agent}, Nilai header Content-Type: {content_type}, Pemilik: {pemilik}'
    
    # Mengembalikan pesan yang berisi nilai header yang diperoleh
    return pesan

# 6. Query String Parameter
@app.route('/search')
def search():
    # Mendapatkan nilai parameter 'query' dari query string menggunakan request.args.get()
    query = request.args.get('query')
    
    # Memeriksa apakah parameter 'query' telah diberikan
    if query:
        # Jika parameter 'query' diberikan, mengembalikan pesan dengan nilai query
        return f'Hasil pencarian untuk: {query}'
    else:
        # Jika parameter 'query' tidak diberikan, mengembalikan pesan error
        return 'Harap masukkan parameter query dalam URL.'

# 7. File Uploads Parameter
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Memeriksa apakah ada file yang diunggah dalam permintaan
        if 'file' not in request.files:
            return 'Tidak ada file yang diunggah.'
        
        file = request.files['file']
        print(file)
        
        # Memeriksa apakah nama file kosong
        if file.filename == '':
            return 'Nama file kosong.'
        
        # Menyimpan file yang diunggah ke folder uploads
        file.save('uploads/' + file.filename)
        
        # Mengembalikan pesan sukses
        return 'File berhasil diunggah.'
    
    # Jika metode permintaan adalah GET, menampilkan formulir unggah file
    return render_template('upload_form.html')

# 8. Cookies Parameter
@app.route('/set_cookie')
def set_cookie():
    # Membuat objek respons
    response = make_response('Cookie berhasil diset.')
    
    # Menambahkan cookie dengan nama 'pengguna' dan nilai 'John Doe' ke respons
    response.set_cookie('pengguna', 'John Doe')
    
    # Mengembalikan respons
    return response

@app.route('/get_cookie')
def get_cookie():
    # Mendapatkan nilai cookie 'pengguna' dari permintaan
    username = request.cookies.get('pengguna')
    
    # Memeriksa apakah cookie ditemukan
    if username:
        return f'Halo, {username}! Selamat datang kembali.'
    else:
        return 'Cookie pengguna tidak ditemukan.'

# 9. Form Data Parameter
@app.route('/submit', methods=['POST'])
def submit_form():
    # Mendapatkan nilai parameter 'username' dari data formulir menggunakan request.form.get()
    username = request.form.get('username')
    
    # Mendapatkan nilai parameter 'password' dari data formulir menggunakan request.form.get()
    password = request.form.get('password')
    
    # Memeriksa apakah kedua parameter telah diberikan
    if username and password:
        # Jika kedua parameter diberikan, melakukan proses autentikasi
        if username == 'user' and password == 'pass':
            return 'Login berhasil!'
        else:
            return 'Kombinasi username dan password salah!'
    else:
        # Jika salah satu atau kedua parameter tidak diberikan, mengembalikan pesan error
        return 'Harap masukkan username dan password.'

# 10. Metadata Parameter
@app.route('/info')
def request_info():
    # Mendapatkan metode permintaan (GET, POST, dll.) menggunakan request.method
    metode = request.method
    
    # Mendapatkan alamat IP klien yang melakukan permintaan menggunakan request.remote_addr
    alamat_ip = request.remote_addr
    
    # Mendapatkan daftar header yang dikirimkan klien menggunakan request.headers
    headers = request.headers
    
    # Membuat pesan yang berisi informasi tentang permintaan
    pesan = f'Metode Permintaan: {metode}\nAlamat IP Klien: {alamat_ip}\nHeader: {headers}'
    
    # Mengembalikan pesan informasi tentang permintaan
    return pesan

if __name__ == '__main__':
    # Menjalankan aplikasi Flask
    app.run(debug=True)



