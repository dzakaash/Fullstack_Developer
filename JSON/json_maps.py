import httplib2  # Mengimpor perpustakaan httplib2, yang membantu kita berinteraksi dengan server menggunakan protokol HTTP.
import json      # Mengimpor modul json, yang digunakan untuk mengonversi data dari dan ke format JSON.

def getGeocodeLocation(inputString):
    # Deklarasi variabel yang berisi kunci API Google yang Anda miliki. 
    # Ganti "PASTE_YOUR_KEY_HERE" dengan kunci Anda.
    google_api_key = "PASTE_YOUR_KEY_HERE"  

    # Mengganti setiap spasi dalam input string dengan tanda tambah (+).
    # Hal ini dilakukan agar input dapat dibaca dengan benar dalam URL.
    locationString = inputString.replace(" ", "+")

    # Membentuk URL untuk mengakses Google Maps Geocoding API dengan 
    # menggunakan alamat dan kunci API.
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (locationString, google_api_key)

    # Membuat objek Http dari kelas httplib2. Objek ini digunakan untuk 
    # melakukan permintaan HTTP.
    h = httplib2.Http()

    # Melakukan permintaan GET ke URL yang telah dibentuk sebelumnya.
    # Respons dari permintaan disimpan dalam variabel response, 
    # sedangkan kontennya disimpan dalam variabel content.
    response, content = h.request(url, 'GET')

    # Mengonversi konten (yang berupa string JSON) menjadi struktur data Python.
    # Ini memungkinkan kita untuk dengan mudah mengakses data di dalamnya.
    result = json.loads(content)

    # Mencetak header respons HTTP. Ini berguna untuk melihat informasi 
    # tambahan dari respons HTTP, seperti status code.
    print("response header: %s \n \n" % response)
    latitude = result['result'][0]['geometry']['location']['lat']
    longitude = result['result'][0]['geometry']['location']['lng']

    # Mengembalikan hasil dari permintaan. Biasanya, hasil ini berupa 
    # data geocode dalam bentuk struktur data Python.
    return (latitude, longitude)

print(getGeocodeLocation("Bandung"))