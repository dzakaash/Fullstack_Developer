import psycopg2
from config import config

# Jika menggunakan config.py
# params = config() # Mengambil parameter koneksi dari file config.py

def connect():
    connection = None
    params = config() # Mengambil parameter koneksi dari file config.py
    print('Menghubungkan ke database PostgreSQL...')
    try:
        connection = psycopg2.connect(**params) # Membuat koneksi ke database menggunakan parameter yang sudah diambil
        # Membuat cursor untuk menjalankan perintah SQL
        crsr = connection.cursor()
        print('Versi database PostgreSQL:')
        crsr.execute('SELECT version()') # Menjalankan perintah SQL untuk mendapatkan versi database
        db_version = crsr.fetchone() # Mengambil hasil perintah SQL
        print(db_version)
        crsr.close() # Menutup cursor setelah selesai
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close() # Menutup koneksi
            print('Koneksi database ditutup.')

if __name__ == "__main__":
    connect() # Memanggil fungsi connect untuk menghubungkan ke database
