# # Ada beberapa cara, teknik, dan trik yang dapat Anda gunakan untuk membuat baris kode dalam fungsi Python 
# # lebih singkat dan padat:

# # 1. **List Comprehensions**: Gunakan list comprehensions untuk membuat loop dan membangun 
# # list dalam satu baris kode.
# # Cara biasa
# squares = []
# for i in range(10):
#     squares.append(i**2)

# # Menggunakan list comprehension
# squares = [i**2 for i in range(10)]

# # 2. **Fungsi Lambda**: Gunakan fungsi lambda untuk membuat fungsi anonim dalam satu baris kode.
# # Cara biasa
# def tambah(a, b):
#     return a + b

# # Menggunakan fungsi lambda
# tambah = lambda a, b: a + b
   
# # 3. **Fungsi Built-in**: Gunakan fungsi built-in seperti `map()`, `filter()`, dan `reduce()` 
# # untuk mengurangi jumlah kode yang harus ditulis.
# # Cara biasa
# numbers = [1, 2, 3, 4, 5]
# doubled = []
# for num in numbers:
#     doubled.append(num * 2)

# # Menggunakan map()
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))

# # 4. **Pendekatan Inline**: Gunakan pendekatan inline untuk kondisi atau operasi yang sederhana.
# # Cara biasa
# if x > 0:
#     hasil = 'positif'
# else:
#     hasil = 'negatif'

# # Pendekatan inline
# hasil = 'positif' if x > 0 else 'negatif'

# # 5. **Multiple Assignment**: Gunakan multiple assignment untuk menukar nilai antar variabel atau 
# # menginisialisasi beberapa variabel dalam satu baris.
# # Cara biasa
# temp = a
# a = b
# b = temp

# # Multiple assignment
# a, b = b, a

# # 6. **Menggunakan Fungsi Built-in**: Manfaatkan fungsi built-in seperti `sum()`, `max()`, dan `min()` 
# # untuk melakukan operasi-operasi umum dengan singkat.
# # Cara biasa
# total = 0
# for num in numbers:
#     total += num

# # Menggunakan sum()
# total = sum(numbers)

# # 7. **Mengurangi Struktur Bersarang**: Hindari struktur bersarang yang terlalu dalam dengan memisahkan 
# # logika ke dalam fungsi-fungsi terpisah.
# # Cara biasa
# for i in range(10):
#     for j in range(10):
#         print(i * j)

# # Menggunakan fungsi terpisah
# def print_multiplication_table():
#     for i in range(10):
#         for j in range(10):
#             print(i * j)

# # 8. **Menggunakan Ekspresi Ternary**: Gunakan ekspresi ternary untuk menggantikan pernyataan if-else yang sederhana.
# # Cara biasa
# if kondisi:
#     hasil = nilai1
# else:
#     hasil = nilai2

# # Menggunakan ekspresi ternary
# hasil = nilai1 if kondisi else nilai2

# # 9. **Pendekatan Inline untuk Loop**: Gunakan pendekatan inline seperti generator expressions 
# # untuk loop yang hanya membutuhkan iterasi sekali.
# # Cara biasa
# hasil = []
# for item in iterable:
#     hasil.append(item * 2)

# # Menggunakan generator expression
# hasil = [item * 2 for item in iterable]
   
# # 10. **Pendekatan Inline untuk Filter**: Gunakan pendekatan inline seperti list comprehension untuk filtering data.
# # Cara biasa
# hasil = []
# for item in iterable:
#     if kondisi:
#         hasil.append(item)

# # Menggunakan list comprehension
# hasil = [item for item in iterable if kondisi]

# # 11. **Menggunakan Fungsi Default Argument**: Gunakan nilai default pada parameter fungsi 
# # untuk mengurangi kode yang berulang.
# # Cara biasa
# def fungsi(arg):
#     if arg is None:
#         arg = default_value

# # Menggunakan nilai default pada parameter
# def fungsi(arg=default_value):
#     # Tidak perlu pengecekan khusus untuk argumen None

# # 12. **Menggunakan Pemformatan String**: Gunakan pemformatan string yang ringkas seperti 
# # f-string untuk menggabungkan variabel ke dalam string.
# # Cara biasa
# hasil = "Nilai: " + str(nilai)

# # Menggunakan f-string
# hasil = f"Nilai: {nilai}"