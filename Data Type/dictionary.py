# membuat dictionary
siswa = {
    "nama": "John Doe",
    "usia": 16,
    "kelas": "11A",
    "nilai": {"matematika": 90, "bahasa_inggris": 85, "sejarah": 78}
}

# mengakses nilai berdasarkan kunci
print("Nama Siswa:", siswa["nama"])
print("Usia Siswa:", siswa["usia"])
print("Nilai Matematika:", siswa["nilai"]["matematika"])
 # output >>>
# Nama Siswa: John Doe
# Usia Siswa: 16
# Nilai Matematika: 90

# menambah nlai baru
siswa["alamat"] = "Jl. Merdeka No.10"
print(siswa)
# output >>>
# Nama Siswa: John Doe
# Usia Siswa: 16
# Nilai Matematika: 90
{'nama': 'John Doe', 'usia': 16, 'kelas': '11A', 'nilai': {'matematika': 90, 'bahasa_inggris': 85, 'sejarah': 78}, 'alamat': 'Jl. Merdeka No.10'} 

# mengubah nilai
siswa["usia"] = 17
print(siswa["usia"]) # output >>> 17

# menghapus item
del siswa["nilai"]["sejarah"]
print(siswa["nilai"]) # output >>> {'matematika': 90, 'bahasa_inggris': 85}

# iterasi melalui kunci
for kunci in siswa:
    print(kunci, ":", siswa[kunci])
# output >>>
# nama : John Doe
# usia : 17
# kelas : 11A
# nilai : {'matematika': 90, 'bahasa_inggris': 85}
# alamat : Jl. Merdeka No.10

# Fungsi-fungsi Dictionary
print("Jumlah Kunci:", len(siswa))
print("Daftar Kunci:", siswa.keys())
print("Daftar Nilai:", siswa.values())
print("Pasangan Kunci-Nilai:", siswa.items())
# output >>>
# Jumlah Kunci: 5
# Daftar Kunci: dict_keys(['nama', 'usia', 'kelas', 'nilai', 'alamat'])       
# Daftar Nilai: dict_values(['John Doe', 17, '11A', {'matematika': 90, 'bahasa_inggris': 85}, 'Jl. Merdeka No.10']) 
# Pasangan Kunci-Nilai: dict_items([('nama', 'John Doe'), ('usia', 17), ('kelas', '11A'), ('nilai', {'matematika': 90, 'bahasa_inggris': 85}), ('alamat', 'Jl. Merdeka No.10')])

# membuat dictionary dari tipe data lain, dari array variabel
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) # output >>> {'name': 'John', 'age': 36, 'country': 'Norway'}

#######################################
# Fungsi Bawaan
#1. len(): Mengembalikan jumlah pasangan kunci-nilai dalam dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
panjang_dict = len(my_dict)
print(panjang_dict)  # Output: 3

#2. keys(): Mengembalikan daftar kunci-kunci dalam dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
daftar_kunci = my_dict.keys()
print(daftar_kunci)  # Output: dict_keys(['a', 'b', 'c'])

#3. values(): Mengembalikan daftar nilai-nilai dalam dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
daftar_nilai = my_dict.values()
print(daftar_nilai)  # Output: dict_values([1, 2, 3])

#4. items(): Mengembalikan daftar tupel pasangan kunci-nilai dalam dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
daftar_item = my_dict.items()
print(daftar_item)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

#5. get(): Mengembalikan nilai yang terkait dengan kunci tertentu. Jika kunci tidak ditemukan, dapat memberikan nilai default.
my_dict = {'a': 1, 'b': 2, 'c': 3}
nilai_a = my_dict.get('a')
nilai_d = my_dict.get('d', 0)  # Default value 0 jika 'd' tidak ditemukan
print(nilai_a)  # Output: 1
print(nilai_d)  # Output: 0

#6. pop(): Menghapus dan mengembalikan nilai yang terkait dengan kunci tertentu.
my_dict = {'a': 1, 'b': 2, 'c': 3}
nilai_b = my_dict.pop('b')
print(my_dict)    # Output: {'a': 1, 'c': 3}
print(nilai_b)    # Output: 2

#7. popitem(): Menghapus dan mengembalikan pasangan kunci-nilai yang terakhir dimasukkan ke dalam dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
pasangan_terakhir = my_dict.popitem()
print(my_dict)           # Output: {'a': 1, 'b': 2}
print(pasangan_terakhir)  # Output: ('c', 3)

#8. update(): Menggabungkan dictionary dengan dictionary lain atau dengan pasangan kunci-nilai baru.
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
dict_a.update(dict_b)
print(dict_a)  # Output: {'a': 1, 'b': 3, 'c': 4}

#9. clear(): Menghapus semua pasangan kunci-nilai dari dictionary, membuat dictionary menjadi kosong.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}
