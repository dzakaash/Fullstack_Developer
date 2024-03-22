from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    # Membuat objek parser
    parser = ConfigParser()
    # Membaca file konfigurasi
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1] # Menyimpan parameter koneksi ke dalam dictionary
    else:
        raise Exception(
            'Bagian {0} tidak ditemukan dalam file {1}.'.format(section, filename))
    return db # Mengembalikan dictionary yang berisi parameter koneksi\
