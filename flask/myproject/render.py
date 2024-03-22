from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
# Rendering template dalam Flask dilakukan dengan menggunakan metode render_template(). Yang harus Anda lakukan adalah memberikan nama template dan variabel yang ingin Anda lewatkan ke mesin template sebagai argumen kata kunci. Berikut adalah contoh sederhana bagaimana cara merender template:
def hello(name=None):
    return render_template('hello.html', name=name)
# Flask akan mencari template dalam folder templates. Jadi jika aplikasi Anda adalah sebuah modul, folder ini berada di sebelah modul tersebut, jika itu adalah sebuah paket, maka sebenarnya berada di dalam paket Anda:
# Kasus 1: sebuah modul:
# /application.py
# /templates
#   /hello.html
# Kasus 2: sebuah paket:
# /application
#   /__init__.py
#   /templates
#       /hello.html
# Untuk template, Anda dapat menggunakan seluruh kekuatan dari template Jinja2. Untuk informasi lebih lanjut, Anda bisa membaca dokumentasi resmi Jinja2 Template.
# Berikut adalah contoh template:
"""
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Halo {{ name }}!</h1>
{% else %}
  <h1>Halo, Dunia!</h1>
{% endif %}
"""
# Di dalam template, Anda juga memiliki akses ke objek config, request, session, dan g, serta fungsi url_for() dan get_flashed_messages().
# Template sangat berguna terutama jika digunakan inheritance. Jika Anda ingin tahu bagaimana itu bekerja, lihat Template Inheritance. Pada dasarnya, template inheritance membuatnya memungkinkan untuk menyimpan elemen-elemen tertentu pada setiap halaman (seperti header, navigasi, dan footer).
# Penghindaran otomatis diaktifkan, jadi jika variabel name berisi HTML, itu akan dihindari secara otomatis. Jika Anda dapat mempercayai suatu variabel dan Anda tahu bahwa itu akan menjadi HTML yang aman (misalnya karena berasal dari modul yang mengonversi markup wiki menjadi HTML), Anda dapat menandainya sebagai aman dengan menggunakan kelas Markup atau dengan menggunakan filter |safe di dalam template. Anda bisa melihat dokumentasi Jinja 2 untuk lebih banyak contoh.
# Berikut adalah pengenalan dasar tentang bagaimana kelas Markup bekerja:
"""
from markupsafe import Markup
Markup('<strong>Halo %s!</strong>') % '<blink>hacker</blink>'
Markup('<strong>Halo &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')
Markup('<em>Marked up</em> &raquo; HTML').striptags()
'Marked up » HTML'
"""

# Uncomment kode di bawah untuk menjalankan aplikasi Flask secara lokal.
if __name__ == '__main__':
    app.run(debug=True)

# Untuk menjalankan aplikasi Flask:
# 1. Pastikan Anda memiliki Flask terinstal di lingkungan Python Anda.
# 2. Simpan skrip ini dengan nama file app.py.
# 3. Buka terminal atau command prompt, lalu arahkan ke direktori tempat file app.py disimpan.
# 4. Jalankan perintah `python app.py`.
# 5. Buka browser dan kunjungi alamat http://127.0.0.1:5000/ untuk melihat hasilnya.
