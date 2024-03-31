from flask import Flask, request, Response

app = Flask(__name__)

# Fungsi untuk memeriksa autentikasi
# Autentikasi: Merujuk pada pembuktian identitas yang benar.
# Otorisasi: Merujuk pada izin untuk melakukan suatu tindakan tertentu.
# Sebuah API mungkin melakukan autentikasi pada Anda tetapi tidak memberi Anda otorisasi untuk melakukan permintaan tertentu.
def check_auth(username, password):
    # Ganti ini dengan sistem autentikasi yang sesuai dengan kebutuhan Anda
    return username == 'admin' and password == 'admin123'

# Fungsi untuk menampilkan pesan kesalahan jika autentikasi gagal
def authentication_required():
    return Response(
        'Autentikasi diperlukan', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

# Fungsi untuk menangani permintaan yang memerlukan autentikasi
@app.route('/')
def index():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authentication_required()
    return 'Halo, {}! Anda berhasil masuk.'.format(auth.username)



#############################
# 1. Basic Authentication dan Bearer Authentication.
# Basic Authentication: Metode autentikasi yang sederhana dan mudah. Pengguna mengirimkan username dan password dalam header permintaan yang dienkripsi dengan Base64.
# Bearer Authentication: Skema autentikasi yang melibatkan penggunaan token keamanan yang disebut bearer tokens. Klien harus mengirimkan token ini dalam header Authorization saat membuat permintaan ke sumber daya yang dilindungi.
# Kedua metode ini memiliki kekurangan dan kelebihan masing-masing, namun keduanya harus digunakan melalui HTTPS (SSL) untuk memastikan keamanan komunikasi.

# Fungsi untuk melakukan autentikasi Basic
def basic_auth(username, password):
    # Ganti ini dengan sistem autentikasi yang sesuai dengan kebutuhan Anda
    return username == 'admin' and password == 'admin123'

# Fungsi untuk menampilkan pesan kesalahan jika autentikasi Basic gagal
def basic_authentication_required():
    return Response(
        'Autentikasi Basic diperlukan', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

# Fungsi untuk menangani permintaan yang memerlukan autentikasi Basic
@app.route('/basic')
def basic():
    auth = request.authorization
    if not auth or not basic_auth(auth.username, auth.password):
        return basic_authentication_required()
    return 'Halo, {}! Anda berhasil masuk menggunakan Basic Authentication.'.format(auth.username)

# Fungsi untuk menampilkan pesan kesalahan jika autentikasi Bearer gagal
def bearer_authentication_required():
    return Response(
        'Autentikasi Bearer diperlukan', 401,
        {'WWW-Authenticate': 'Bearer realm="Token Required"'}
    )

# Fungsi untuk menangani permintaan yang memerlukan autentikasi Bearer
@app.route('/bearer')
def bearer():
    token = request.headers.get('Authorization')
    if not token or not token.startswith('Bearer '):
        return bearer_authentication_required()
    # Ganti ini dengan proses validasi token sesuai kebutuhan Anda
    return 'Halo! Anda berhasil masuk menggunakan Bearer Authentication.'

###########################
# 2. API Keys sebagai salah satu metode autentikasi dalam keamanan REST API. API Keys adalah nilai unik yang diberikan kepada pengguna untuk membuktikan identitas mereka saat melakukan akses ke sistem atau layanan tertentu. Meskipun API Keys adalah metode yang sederhana, namun tidak dianggap sebagai langkah keamanan yang kuat karena potensi kerentanan keamanan yang dimilikinya. Salah satu masalahnya adalah bahwa API Keys seringkali ditransmisikan dengan mudah dan dapat ditemukan oleh pihak yang tidak berwenang. Meskipun demikian, API Keys masih digunakan dalam berbagai kasus penggunaan karena sifatnya yang sederhana dan mudah diimplementasikan. Namun, penting untuk melakukan pengujian keamanan secara teratur untuk memeriksa kerentanan yang mungkin ada dalam sistem autentikasi API Keys.
# Daftar API keys yang valid
valid_api_keys = {
    '1234567890abcdef': 'user1',
    '0987654321abcdef': 'user2'
}

# Fungsi untuk memeriksa kevalidan API key
def check_api_key(api_key):
    return api_key in valid_api_keys

# Fungsi untuk menampilkan pesan kesalahan jika autentikasi API key gagal
def api_key_authentication_required():
    return Response(
        'Autentikasi API key diperlukan', 401,
        {'WWW-Authenticate': 'Apikey realm="API Key Required"'}
    )

# Fungsi untuk menangani permintaan yang memerlukan autentikasi API key
@app.route('/api', methods=['GET'])
def api():
    api_key = request.headers.get('Authorization')
    if not api_key or not check_api_key(api_key):
        return api_key_authentication_required()
    return 'Halo, {}! Anda berhasil masuk menggunakan API Key.'.format(valid_api_keys[api_key])

###########################
# 3. OAuth 2.0 yang digunakan untuk mengamankan layanan web dan API. OAuth 2.0 memperkenalkan perubahan signifikan dari versi sebelumnya, di mana tidak lagi diperlukan untuk menandatangani setiap panggilan dengan hash terenkripsi. Protokol ini menggunakan dua jenis token utama: access token dan refresh token. Access token digunakan untuk mengakses data pengguna, sementara refresh token digunakan untuk mendapatkan access token baru jika yang lama telah kedaluwarsa. OAuth 2.0 menggabungkan autentikasi dan otorisasi untuk memberikan kontrol yang lebih canggih terhadap lingkup (scope) dan validitas akses. Terdapat beberapa alur (flow) yang populer dalam OAuth 2.0, seperti authorization code flow, implicit flow, resource owner password flow, dan client credentials flow. Secara umum, OAuth 2.0 dianggap sebagai pilihan terbaik untuk mengidentifikasi akun pengguna dan memberikan izin yang tepat, karena lebih aman dan kuat daripada pendekatan lainnya.
registered_users = {
    'user1': 'password1',
    'user2': 'password2'
}

# Fungsi untuk memeriksa kevalidan pengguna
def check_user(username, password):
    return username in registered_users and registered_users[username] == password

# Fungsi untuk menghasilkan access token (dalam kasus ini, hanya mengembalikan username)
def generate_access_token(username):
    return username

# Endpont untuk autentikasi menggunakan OAuth 2.0 Authorization Code Flow
@app.route('/oauth/authorization-code', methods=['POST'])
def authorization_code_flow():
    # Mendapatkan username dan password dari permintaan
    username = request.form.get('username')
    password = request.form.get('password')

    # Memeriksa kevalidan pengguna
    if check_user(username, password):
        # Menghasilkan access token
        access_token = generate_access_token(username)
        return f'Access token: {access_token}', 200
    else:
        return 'Autentikasi gagal', 401
##########################
# 4. OpenID Connect, yang merupakan lapisan identitas yang sederhana di atas protokol OAuth 2.0. OpenID Connect memungkinkan aplikasi klien untuk memverifikasi identitas pengguna dan memperoleh informasi profil dasar pengguna dengan cara yang interoperabel dan mirip dengan REST. Protokol ini menggunakan JSON sebagai format data dan mendefinisikan mekanisme penemuan untuk mendapatkan metadata server OpenID. OpenID Connect memungkinkan berbagai jenis klien, termasuk web, mobile, dan JavaScript, untuk berinteraksi dengan server autentikasi dan memperoleh informasi tentang pengguna. Salah satu fitur utamanya adalah penggunaan JSON Web Tokens (JWT) untuk mengenkripsi informasi identitas pengguna. Dengan OpenID Connect, aplikasi dapat memperoleh informasi autentikasi dan otorisasi yang aman dan terpercaya.
# Endpoint untuk autentikasi menggunakan OpenID Connect Discovery
@app.route('/openid/discovery', methods=['GET'])
def openid_discovery():
    # URL untuk OpenID Connect Discovery
    discovery_url = 'https://server.com/openid-configuration'

    # Mendapatkan metadata OpenID dari server
    openid_metadata = request.get(discovery_url).json()

    return openid_metadata, 200

if __name__ == '__main__':
    app.run(debug=True)
