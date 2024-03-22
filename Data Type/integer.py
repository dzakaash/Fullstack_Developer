x = 1 #integer
y = 2.8 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))

a = float(x) #ubah ke float
b = int(y) #ubah ke integer
c = complex(x) #ubah ke complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

m = 25
n = 5

o = m+n
p = m-n
q = m*n
r = m/n
s = m**n

print(o)
print(p)
print(q)
print(r)
print(s)

nilai = 80
# def penilaian(nilai):
if nilai < 50:
    print("D")
elif nilai < 70:
    print("C")
elif nilai < 80:
    print("B")
else:
    print("A")
# penilaian(nilai)

angka = 1
while angka <= 5: #while loop
    print(angka)
    angka += 1 #pembaruan angka untuk pembatas

buah = ["apel", "mangga", "jeruk"]
for buah_favorit in buah : #for loop
    print("Saya suka", buah_favorit)

#Return
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

# Memanggil fungsi dan menyimpan nilai kembalian
hasil_penambahan = tambah(22, 7)

# Menampilkan hasil
print("Hasil penambahan:", hasil_penambahan)
#output 'Hasil penambahan: 29'

############################################
#Bedah Fungsi Bawaan
#1. int(): Mengonversi nilai menjadi tipe data integer. Jika nilai desimal, maka akan dibulatkan ke bawah.
angka_desimal = 5.8
angka_integer = int(angka_desimal)
print(angka_integer)  # Output: 5

#2. abs(): Mengembalikan nilai absolut dari suatu angka (jarak angka tersebut dari nol).
angka_negatif = -7
nilai_absolut = abs(angka_negatif)
print(nilai_absolut)  # Output: 7
# Tanpa menggunakan fungsi bawaan abs()
angka = -10 # Langkah 1: Inisialisasi angka
if angka < 0: # Langkah 2: Periksa apakah angka negatif
    nilai_absolut = -angka # Jika angka negatif, ubah tanda menjadi positif
else:
    nilai_absolut = angka # Jika angka tidak negatif, nilai absolut sama dengan angka itu sendiri
print(f"Nilai absolut dari {angka} adalah: {nilai_absolut}") # Output: "Nilai absolut dari -10 adalah: 10"

#3. round(): Membulatkan nilai ke bilangan bulat terdekat atau ke jumlah tempat desimal tertentu.
angka_decimal = 3.75
hasil_bulat = round(angka_decimal)
print(hasil_bulat)  # Output: 4
# Tanpa menggunakan fungsi bawaan round()
angka = 3.14159 # Langkah 1: Inisialisasi angka dan jumlah digit desimal
digit_desimal = 2
angka_kali_10 = angka * (10 ** digit_desimal) # Langkah 2: Mengalikan angka dengan 10 pangkat digit_desimal untuk memindahkan digit desimal ke digit pertama
angka_kali_10_plus_05 = angka_kali_10 + 0.5 # Langkah 3: Menambahkan 0.5 untuk melakukan pembulatan
angka_bulat = int(angka_kali_10_plus_05) # Langkah 4: Mengkonversi hasil penambahan menjadi bilangan bulat
angka_bulat_kembali = angka_bulat / (10 ** digit_desimal) # Langkah 5: Mengalikan kembali dengan 10 pangkat -digit_desimal untuk mengembalikan digit desimal ke posisi semula
print(f"Hasil pembulatan dari {angka} adalah: {angka_bulat_kembali}") # Output: "Hasil pembulatan dari 3.14159 adalah: 3.14"

#4. max() dan min(): Mengembalikan nilai maksimum atau minimum dari sejumlah nilai.
nilai_max = max(10, 5, 8, 12)
nilai_min = min(10, 5, 8, 12)
print(nilai_max)  # Output: 12
print(nilai_min)  # Output: 5
# Tanpa menggunakan fungsi bawaan max()
list_angka = [10, 5, 8, 15] # Langkah 1: Inisialisasi list angka
nilai_maksimum = list_angka[0] # Langkah 2: Inisialisasi variabel untuk menyimpan nilai maksimum
for angka in list_angka: # Langkah 3: Iterasi setiap nilai dalam list
    if angka > nilai_maksimum: # Langkah 4: Perbandingkan dengan nilai maksimum saat ini
        nilai_maksimum = angka
print(f"Nilai maksimum dari {list_angka} adalah: {nilai_maksimum}") # Output: "Nilai maksimum dari [10, 5, 8, 15] adalah: 15"
# Tanpa menggunakan fungsi bawaan min()
list_angka = [10, 5, 8, 15] # Langkah 1: Inisialisasi list angka
nilai_minimum = list_angka[0] # Langkah 2: Inisialisasi variabel untuk menyimpan nilai minimum
for angka in list_angka: # Langkah 3: Iterasi setiap nilai dalam list
    if angka < nilai_minimum: # Langkah 4: Perbandingkan dengan nilai minimum saat ini
        nilai_minimum = angka
print(f"Nilai minimum dari {list_angka} adalah: {nilai_minimum}") # Output: "Nilai minimum dari [10, 5, 8, 15] adalah: 5"

#5. sum(): Menghitung jumlah semua elemen dalam suatu iterable (seperti list atau tuple).
angka_list = [2, 4, 6, 8]
total = sum(angka_list)
print(total)  # Output: 20
# Tanpa menggunakan fungsi bawaan sum()
list_angka = [1, 2, 3, 4, 5] # Langkah 1: Inisialisasi list angka
total = 0 # Langkah 2: Inisialisasi variabel untuk menyimpan total
for angka in list_angka: # Langkah 3: Iterasi setiap nilai dalam list
    total += angka # Langkah 4: Tambahkan nilai ke total saat ini
print(f"Total dari {list_angka} adalah: {total}") # Output: "Total dari [1, 2, 3, 4, 5] adalah: 15"

#6. divmod(): Mengembalikan pasangan (divmod) hasil bagi dan sisa bagi dari dua angka.
hasil_divmod = divmod(10, 3)
print(hasil_divmod)  # Output: (3, 1) - karena 10 dibagi 3 hasilnya 3 dengan sisa 1
# Tanpa menggunakan fungsi bawaan divmod()
bilangan_dibagi = 10  # Langkah 1: Inisialisasi bilangan yang akan dibagi dan pembagi
pembagi = 3
hasil_pembagian_manual = bilangan_dibagi // pembagi # Langkah 2: Hitung hasil pembagian secara manual
sisa_bagi_manual = bilangan_dibagi % pembagi # Langkah 3: Hitung sisa bagi secara manual
print(f"Hasil pembagian dari {bilangan_dibagi} / {pembagi} adalah: {hasil_pembagian_manual}")
print(f"Sisa bagi dari {bilangan_dibagi} / {pembagi} adalah: {sisa_bagi_manual}")
# Output: "Hasil pembagian dari 10 / 3 adalah: 3"
#         "Sisa bagi dari 10 / 3 adalah: 1"

#7. pow(): Menghitung pangkat dari suatu angka.
hasil_pangkat = pow(2, 3)  # sama dengan 2^3
print(hasil_pangkat)  # Output: 8
# Tanpa menggunakan fungsi bawaan pow()
basis = 2 # Langkah 1: Inisialisasi bilangan yang akan dipangkatkan dan pangkat
pangkat = 3
hasil_pemangkatan_manual = basis ** pangkat # Langkah 2: Hitung hasil pemangkatan secara manual
print(f"Hasil {basis} pangkat {pangkat} adalah: {hasil_pemangkatan_manual}") # Output: "Hasil 2 pangkat 3 adalah: 8"

# ############################################
# # RUMUS

# # 1. **Rumus Ekspresi untuk Menjumlahkan Elemen dalam List**:
# total = sum(list)

# # 2. **Rumus Ekspresi untuk Mencari Nilai Maksimum dalam List**:
# maksimum = max(list)

# # 3. **Rumus Ekspresi untuk Mencari Nilai Minimum dalam List**:
# minimum = min(list)

# # 4. **Rumus Ekspresi untuk Menghitung Jumlah Kemunculan Elemen Tertentu dalam List**:
# jumlah_kemunculan = list.count(nilai)

# # 5. **Rumus Ekspresi untuk Menggabungkan String dalam List menjadi Satu String**:
# gabung = ''.join(list_of_strings)

# # 6. **Rumus Ekspresi untuk Menemukan Panjang String Terpanjang dalam List**:
# panjang_terpanjang = max(len(string) for string in list_of_strings)

# # 7. **Rumus Ekspresi untuk Mengalikan Semua Elemen dalam List**:
# hasil_kali = 1
# for elemen in list:
#     hasil_kali *= elemen

# # 8. **Rumus Ekspresi untuk Memfilter List berdasarkan Kondisi Tertentu**:
# hasil_filter = [elemen for elemen in list if kondisi]

# # 9. **Rumus Ekspresi untuk Mencari Nilai Unik dalam List**:
# nilai_unik = list(set(list))

# # 10. **Rumus Ekspresi untuk Mengambil 5 Elemen Pertama dari List**:
# lima_elemen_pertama = list[:5]

# # 11. **Rumus Ekspresi untuk Menemukan Nilai Terbesar dari Dua Variabel**:
# maksimum = max(variabel1, variabel2)

# # 12. **Rumus Ekspresi untuk Menemukan Nilai Absolut**:
# nilai_absolut = abs(angka)

# # 13. **Rumus Kuadrat**:
# hasil_kuadrat = angka ** 2

# # 14. **Rumus Akar Kuadrat**:
# akar_kuadrat = angka ** 0.5

# # 15. **Rumus Persegi Panjang**:
# luas_persegi_panjang = panjang * lebar
# keliling_persegi_panjang = 2 * (panjang + lebar)

# # 16. **Rumus Lingkaran**:
# import math

# luas_lingkaran = math.pi * (jari_jari ** 2)
# keliling_lingkaran = 2 * math.pi * jari_jari

# # 17. **Rumus Segitiga**:
# luas_segitiga = 0.5 * alas * tinggi

# # 18. **Rumus Trigonometri** (sin, cos, tan):
# import math

# nilai_sin = math.sin(sudut)
# nilai_cos = math.cos(sudut)
# nilai_tan = math.tan(sudut)

# # 19. **Rumus Logaritma**:
# import math

# nilai_log = math.log(10)

# # 20. **Rumus Faktorial**:
# import math

# nilai_faktorial = math.factorial(5)  # Contoh untuk 5!

# # 21. **Rumus Deret Aritmatika**:
# jumlah_deret_aritmatika = (n / 2) * (2 * a + (n - 1) * d)

# # 22. **Rumus Deret Geometri**:
# jumlah_deret_geometri = a * ((1 - r**n) / (1 - r))

# # 23. **Rumus Persentase**:
# persentase = (nilai / total) * 100

# # 24. **Rumus Regresi Linear**:
# from scipy import stats

# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# # 25. **Rumus Persamaan Kuadratik**:
# import math

# a = 1
# b = 5
# c = 6

# diskriminan = b**2 - 4*a*c
# if diskriminan > 0:
#     akar1 = (-b + math.sqrt(diskriminan)) / (2*a)
#     akar2 = (-b - math.sqrt(diskriminan)) / (2*a)
# elif diskriminan == 0:
#     akar1 = akar2 = -b / (2*a)
# else:
#     real_part = -b / (2*a)
#     imaginary_part = math.sqrt(abs(diskriminan)) / (2*a)
#     akar1 = complex(real_part, imaginary_part)
#     akar2 = complex(real_part, -imaginary_part)

# # 26. **Rumus Eksponensial**:
# eksponensial = math.exp(x)

# # 27. **Rumus Logaritma Natural**:
# logaritma_natural = math.log(x)

# # 28. **Rumus Nilai Mutlak**:
# nilai_mutlak = abs(angka)

# # 29. **Rumus Permutasi dan Kombinasi**:
# from math import factorial

# permutasi = factorial(n) / factorial(n - r)
# kombinasi = factorial(n) / (factorial(r) * factorial(n - r))

# # 30. **Rumus Median**:
# median = sorted(list)[len(list) // 2] if len(list) % 2 != 0 else (sorted(list)[len(list) // 2 - 1] + sorted(list)[len(list) // 2]) / 2

# # 31. **Rumus Modulus**:
# hasil_modulus = angka1 % angka2

# # 32. **Rumus Integral** (dengan bantuan pustaka seperti SciPy):
# from scipy.integrate import quad

# hasil_integral, _ = quad(fungsi, batas_bawah, batas_atas)

# # 33. **Rumus Standar Deviasi**:
# import statistics

# standar_deviasi = statistics.stdev(data)

# # 34. **Rumus Korelasi Pearson**:
# from scipy.stats import pearsonr

# koefisien_korelasi, _ = pearsonr(data1, data2)

# # 35. **Rumus Regresi Linear Berganda**:
# from sklearn.linear_model import LinearRegression

# model = LinearRegression().fit(X, y)