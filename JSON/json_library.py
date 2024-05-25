import httplib2  # Mengimpor perpustakaan httplib2, yang membantu kita berinteraksi dengan server menggunakan protokol HTTP.
import json      # Mengimpor modul json, yang digunakan untuk mengonversi data dari dan ke format JSON.

def getBooks():
    # Mendefinisikan URL yang akan diakses untuk mengambil informasi 
    # buku dari Open Library API.
    url = "https://openlibrary.org/api/books?bibkeys=ISBN:0201558025,LCCN:93005405&format=json"

    # Membuat objek Http dari kelas httplib2 untuk melakukan permintaan HTTP.
    h = httplib2.Http()

    # Melakukan permintaan GET ke URL yang telah ditentukan.
    # Respons dari permintaan disimpan dalam variabel response, 
    # sedangkan kontennya disimpan dalam variabel content.
    response, content = h.request(url, 'GET')
    print(f"ini RESPONSE {response}")
    print(f"ini CONTENT {content}")
    
    
    # print(type(content))
    # print(content)

    # Mengonversi konten (string JSON) menjadi struktur data Python.
    # Ini memungkinkan kita untuk dengan mudah mengakses data di dalamnya.
    result = json.loads(content)
    
    # print(type(result))

    # Mengembalikan hasil dari permintaan. Biasanya, hasil ini berupa 
    # data buku dalam bentuk struktur data Python.
    return result

# Memanggil fungsi getBooks() untuk mendapatkan data buku.
# result fungsi kita jadikan variabel data
data = getBooks()

# Mencetak URL pratinjau (preview URL) buku dengan nomor ISBN:0201558025 
# dari data yang diterima.
print(data["ISBN:0201558025"]["preview_url"])