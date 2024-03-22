fruit = "banana"
colour = "yellow"

print(fruit + " " + colour) #penggabungan
print(fruit*2) #pengulangan

letter = fruit[1] #select character berdsarkan indeks
print(letter)

len(fruit) #panjang indeks string
print(len(fruit))

fruit_besar = fruit.upper() #mengkapitalisasi
print(fruit_besar)

apel_besar = "APEL"
apel_kecil = apel_besar.lower() #mengecilkan huruf
print(apel_kecil)

cek_substring = "na" in fruit #mengecek isi dalam string
print(cek_substring)

ganti = fruit.replace("nana", "nunu") #mengganti
print(ganti)

selamat_pagi = "Good, morning world!"
pecah = selamat_pagi.split(", ") #memisahkan teks
print(pecah)

selamat_pagi2 = "         Good, morning world!"
bersih = selamat_pagi2.strip() #membersihkan white space sebelum dan setelah kalimat
print(bersih)

index = 0
while index < len(fruit): #while loop tiap karakter di fruit selama memenuhi syarat
    letter = fruit[index]
    print(letter)
    index = index + 1

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes: #for loop tiap karakter di prefixes
    print (letter + suffix)

s = "Peter, Paul, Mary"
print(s[0:5]) #slice karakter 0-5
print(s[7:11]) #slice karakter 7-11
print(s[17:21]) #slice karakter 17-21
print(fruit[:3]) #slice karakter 0-3
print(fruit[3:]) #slice karakter 4-terakhir

count = 0
for char in fruit: #looping and counting
    if char == 'a':
        count = count + 1
print(count)

#find function
def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1

# #find function
# import string
# index = string.find(fruit, "a")
# print(index)

# #character classification
# def isLower(ch):
#     return string.find(string.lowercase, ch) != -1
# def isLower(ch):
#     return ch in string.lowercase
# def isLower(ch):
#     return 'a' <= ch <= 'z'

#string bisa menggunakan dua kutipan atau satu
print("Hello")
print('Hello')

#membuat variabel dari string
a = "Hello"
print(a)

#print 3 baris, gunakan 3 kutipan
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1]) #print string berdasarkan indeks

############################################
# Fungsi Bawaan
#1. len(): Mengembalikan panjang (jumlah karakter) dari suatu string.
# Fungsi ini memungkinkan kita untuk dengan mudah mendapatkan informasi tentang banyaknya elemen atau panjang dari objek tersebut.
kata = "Python"
panjang_kata = len(kata)
print(panjang_kata)  # Output: 6
# iterasi
my_list = [1, 2, 3, 4, 5]
panjang_list = 0
for elemen in my_list:
    panjang_list += 1
print(panjang_list)  # Output: 5
# rekursi
def hitung_panjang(obj):
    if not obj:
        return 0
    else:
        return 1 + hitung_panjang(obj[1:])
my_list = [1, 2, 3, 4, 5]
panjang_list = hitung_panjang(my_list)
print(panjang_list)  # Output: 5

#2. str(): Mengonversi nilai menjadi tipe data string.
angka = 42
angka_string = str(angka)
print(angka_string)  # Output: "42"

#3. upper() dan lower(): Mengubah string menjadi huruf kapital atau huruf kecil.
kalimat = "Belajar Python"
kapital = kalimat.upper()
kecil = kalimat.lower()
print(kapital)  # Output: "BELAJAR PYTHON"
print(kecil)    # Output: "belajar python"
# iterasi
teks = "contoh string" # Langkah 1: Inisialisasi string input
teks_kapital = "" # Langkah 2: Membuat string kosong untuk menyimpan hasil
for karakter in teks: # Langkah 3: Iterasi setiap karakter dalam string input
    if 'a' <= karakter <= 'z': # Langkah 4: Cek apakah karakter adalah huruf kecil
        teks_kapital += chr(ord(karakter) - ord('a') + ord('A')) # Jika ya, tambahkan karakter kapital ke string hasil. ord() untuk dapatkan nilai unicode, chr() untuk dapatkan karakter dari unicode
    else:
        teks_kapital += karakter # Jika bukan huruf kecil, tambahkan karakter aslinya ke string hasil
print(teks_kapital)  # Output: "CONTOH STRING"

#4. capitalize() dan title(): Mengubah huruf pertama setiap kata menjadi huruf kapital.
kalimat = "belajar bahasa python"
kapital_pertama = kalimat.capitalize()
kapital_setiap_kata = kalimat.title()
print(kapital_pertama)       # Output: "Belajar bahasa python"
print(kapital_setiap_kata)   # Output: "Belajar Bahasa Python"
# iterasi capitalize()
kalimat = "contoh kalimat" # Langkah 1: Inisialisasi string input
kalimat_terkapital = "" # Langkah 2: Membuat string kosong untuk menyimpan hasil
huruf_pertama = True # Langkah 3: Inisialisasi variabel untuk menandai huruf pertama
for karakter in kalimat: # Langkah 4: Iterasi setiap karakter dalam string input
    if huruf_pertama: # Langkah 5: Jika karakter adalah huruf pertama
        kalimat_terkapital += karakter.upper() # Tambahkan karakter kapital ke string hasil
        huruf_pertama = False # Set variabel huruf_pertama menjadi False untuk karakter berikutnya
    else:
        kalimat_terkapital += karakter # Jika bukan huruf pertama, tambahkan karakter aslinya ke string hasil
        if karakter == ' ': # Jika karakter adalah spasi, set huruf_pertama menjadi True untuk kata berikutnya
            huruf_pertama = True
# iterasi title()
kalimat = "contoh kalimat" # Langkah 1: Inisialisasi string input
kalimat_berjudul = "" # Langkah 2: Membuat string kosong untuk menyimpan hasil
for indeks in range(len(kalimat)): # Langkah 3: Iterasi setiap karakter dalam string input
    if indeks == 0 or kalimat[indeks - 1] == ' ': # Langkah 4: Jika karakter adalah huruf pertama atau setelah spasi
        kalimat_berjudul += kalimat[indeks].upper() # Tambahkan karakter kapital ke string hasil
    else:
        kalimat_berjudul += kalimat[indeks] # Jika bukan huruf pertama, tambahkan karakter aslinya ke string hasil
print(kalimat_berjudul)  # Output: "Contoh Kalimat"
print(kalimat_terkapital)  # Output: "Contoh kalimat"

#5. split(): Membagi string menjadi list berdasarkan pemisah tertentu.
kalimat = "Hari ini cuaca bagus"
kata_kalimat = kalimat.split()
print(kata_kalimat)  # Output: ['Hari', 'ini', 'cuaca', 'bagus']
# iterasi
kalimat = "Ini adalah contoh kalimat" # Langkah 1: Inisialisasi string input
potongan_kalimat = [] # Langkah 2: Membuat list kosong untuk menyimpan potongan-potongan
potongan_saat_ini = "" # Langkah 3: Inisialisasi variabel untuk menyimpan potongan saat ini
for karakter in kalimat: # Langkah 4: Iterasi setiap karakter dalam string input
    if karakter != ' ': # Langkah 5: Jika karakter bukan spasi, tambahkan ke potongan saat ini
        potongan_saat_ini += karakter
    else:
        potongan_kalimat.append(potongan_saat_ini) # Jika karakter adalah spasi, tambahkan potongan saat ini ke list
        potongan_saat_ini = "" # Reset potongan saat ini menjadi string kosong
potongan_kalimat.append(potongan_saat_ini) # Langkah 6: Tambahkan potongan terakhir setelah loop selesai
print(potongan_kalimat) # Output: ['Ini', 'adalah', 'contoh', 'kalimat']

#6. join(): Menggabungkan elemen-elemen suatu iterable (seperti list) menjadi string.
kata_list = ['Hari', 'ini', 'cuaca', 'bagus']
kalimat_gabung = ' '.join(kata_list)
print(kalimat_gabung)  # Output: "Hari ini cuaca bagus"
# iterasi
list_kata = ["Ini", "adalah", "contoh", "kalimat"] # Langkah 1: Inisialisasi list input
kalimat_gabung = "" # Langkah 2: Inisialisasi string kosong untuk menyimpan hasil
kata_pertama = True # Langkah 3: Inisialisasi variabel untuk menentukan apakah kata pertama atau bukan
for kata in list_kata: # Langkah 4: Iterasi setiap kata dalam list
    if not kata_pertama: # Langkah 5: Jika bukan kata pertama, tambahkan spasi sebagai pemisah
        kalimat_gabung += " "
    kalimat_gabung += kata # Langkah 6: Tambahkan kata ke string hasil
    kata_pertama = False # Set kata_pertama menjadi False setelah iterasi pertama
print(kalimat_gabung) # Output: "Ini adalah contoh kalimat"

#7. strip(), lstrip(), dan rstrip(): Menghapus spasi atau karakter tertentu dari awal (kiri), akhir (kanan), atau kedua sisi (kedua) string.
teks = "   Contoh String   "
tanpa_spasi = teks.strip()
print(tanpa_spasi)  # Output: "Contoh String"
# iterasi strip()
teks = "   Contoh String   " # Langkah 1: Inisialisasi string input
indeks_awal = 0 # Langkah 2: Inisialisasi indeks awal dan akhir untuk potongan string
indeks_akhir = len(teks) - 1
while indeks_awal <= indeks_akhir and teks[indeks_awal].isspace(): # Langkah 3: Pindahkan indeks_awal ke kanan sampai karakter bukan whitespace
    indeks_awal += 1
while indeks_akhir >= indeks_awal and teks[indeks_akhir].isspace(): # Langkah 4: Pindahkan indeks_akhir ke kiri sampai karakter bukan whitespace
    indeks_akhir -= 1
teks_strip = teks[indeks_awal:indeks_akhir+1] # Langkah 5: Ambil potongan string dari indeks_awal hingga indeks_akhir
print(teks_strip) # Output: "Contoh String"

#8. replace(): Menggantikan suatu substring dengan substring lain dalam string.
kalimat = "Saya suka programming"
kalimat_baru = kalimat.replace("suka", "gemar")
print(kalimat_baru)  # Output: "Saya gemar programming"
# iterasi
teks = "Ini adalah contoh kalimat" # Langkah 1: Inisialisasi string input
teks_ganti = "" # Langkah 2: Inisialisasi string untuk menyimpan hasil
substring_ganti = "contoh" # Langkah 3: Inisialisasi substring yang akan diganti dan substring pengganti
substring_pengganti = "sebuah"
posisi = 0 # Langkah 4: Inisialisasi variabel untuk melacak posisi saat ini dalam string
while posisi < len(teks): # Langkah 5: Cari setiap kemunculan substring yang akan diganti
    indeks = -1  # Langkah 6: Temukan indeks substring yang akan diganti secara manual
    for i in range(posisi, len(teks) - len(substring_ganti) + 1):
        if teks[i:i+len(substring_ganti)] == substring_ganti:
            indeks = i
            break
    if indeks == -1:
        teks_ganti += teks[posisi:] # Jika tidak ditemukan lagi, tambahkan sisa string ke hasil dan keluar dari loop
        break
    else:
        teks_ganti += teks[posisi:indeks] # Tambahkan bagian string sebelum kemunculan substring yang akan diganti
        teks_ganti += substring_pengganti # Tambahkan substring pengganti
        posisi = indeks + len(substring_ganti) # Pindahkan posisi ke setelah kemunculan substring yang akan diganti
print(teks_ganti) # Output: "Ini adalah sebuah kalimat"

#9. enumerate(): untuk mengembalikan indeks dan nilai dari suatu iterable, seperti list atau string, dalam bentuk tuple.
# Fungsi ini membantu dalam melakukan iterasi pada suatu iterable sambil melacak indeksnya.
# Menggunakan fungsi bawaan enumerate()
list_angka = [10, 20, 30, 40]
for indeks, nilai in enumerate(list_angka):
    print(f"Indeks: {indeks}, Nilai: {nilai}")
# Output:
# Indeks: 0, Nilai: 10
# Indeks: 1, Nilai: 20
# Indeks: 2, Nilai: 30
# Indeks: 3, Nilai: 40
#iterasi
list_angka = [10, 20, 30, 40] # Langkah 1: Inisialisasi list input
indeks = 0 # Langkah 2: Inisialisasi variabel indeks
for nilai in list_angka: # Langkah 3: Iterasi setiap nilai dalam list
    print(f"Indeks: {indeks}, Nilai: {nilai}") # Langkah 4: Tampilkan indeks dan nilai
    indeks += 1 # Langkah 5: Tingkatkan nilai indeks
# Output:
# Indeks: 0, Nilai: 10
# Indeks: 1, Nilai: 20
# Indeks: 2, Nilai: 30
# Indeks: 3, Nilai: 40

#10. isspace():  digunakan untuk memeriksa apakah semua karakter dalam suatu string adalah whitespace (spasi, tab, newline, dll.)
# Kasus 1: Semua karakter adalah whitespace
teks_1 = "    \t\n"
if teks_1.isspace():
    print("Semua karakter dalam teks_1 adalah whitespace.")
else:
    print("Tidak semua karakter dalam teks_1 adalah whitespace.")
# Kasus 2: Terdapat karakter non-whitespace
teks_2 = "  Ini adalah teks  "
if teks_2.isspace():
    print("Semua karakter dalam teks_2 adalah whitespace.")
else:
    print("Tidak semua karakter dalam teks_2 adalah whitespace.")

#11. find():  digunakan untuk mencari indeks dari suatu substring dalam sebuah string.
# Fungsi ini mengembalikan indeks pertama dari kemunculan substring tersebut, atau -1 jika substring tidak ditemukan. 
teks = "Ini adalah contoh kalimat"
indeks = teks.find("contoh")
print(f"Indeks pertama dari 'contoh' adalah: {indeks}") # Output: "Indeks pertama dari 'contoh' adalah: 11"
# Iterasi
teks = "Ini adalah contoh kalimat" # Langkah 1: Inisialisasi string input
substring_cari = "contoh" # Langkah 2: Inisialisasi substring yang akan dicari
indeks_pertama = -1 # Langkah 3: Inisialisasi variabel untuk menyimpan indeks pertama kemunculan substring
posisi = 0 # Langkah 4: Inisialisasi variabel untuk melacak posisi saat ini dalam string
while posisi <= len(teks) - len(substring_cari): # Langkah 5: Cari indeks pertama kemunculan substring secara manual
    if teks[posisi:posisi+len(substring_cari)] == substring_cari:
        indeks_pertama = posisi
        break  # Hentikan iterasi jika substring ditemukan
    posisi += 1
print(f"Indeks pertama dari '{substring_cari}' adalah: {indeks_pertama}") # Output: "Indeks pertama dari 'contoh' adalah: 11"