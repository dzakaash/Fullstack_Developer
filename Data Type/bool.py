for x in "banana": #print karakter satu per satu
    print(x)

txt = "The best things in life are free!"
print("free" in txt) #untuk memeriksa apakah ada frasa atau karakter tertentu dalam string

if "free" in txt: #print dengan hanya jika
    print("Yes, 'free' is present.")

print("expensive" not in txt) #untuk memeriksa apakah frasa tertentu tidak ada dalam sring

if "expensive" not in txt: #print dengan hanya jika
    print("No, 'expensive' is NOT present.")
    
x = 5
y = 10
if x > 0 and y > 0: #fungsi and
    print("Kedua nilai positif")
    
hari = "Minggu"
if hari == "Sabtu" or hari == "Minggu": #fungsi or
    print("Hari libur akhir pekan")
    
cuaca_baik = True
if not cuaca_baik: #fungsi not
    print("Bawa payung!")

nilai = 85
if nilai >=70 and nilai <= 90: #kombinasi operator logika
    print("Nilai dalam rentang yang baik")

usia = 25
status_pekerjaan = "Pegawai"
if usia >= 21 and status_pekerjaan == "Pegawai": #untuk stuktur pernyataan kondisional
    print("anda memenuhi syarat untuk pinjaman")
    
#comparison
word = "banana" 
if word == "banana":
    print("Yes, we have no bananas!")
if word < "banana":
    print("Your word," + word + "comes before banana.")
elif word > "banana":
    print("Your word," + word + ",comes after banana.")
else:
    print("Yes, we have no bananas!")
    
#nested conditionals
nilai_ujian = 85
peringkat_siswa = 20

if nilai_ujian >= 80:
    print("Anda lolos ujian.")
    if peringkat_siswa <= 30:
        print("Anda mendapatkan peringkat yang baik.")
    else:
        print("Anda perlu meningkatkan peringkat untuk mendapatkan beasiswa.")
else:
    print("Maaf, Anda belum lolos ujian.")
    
#####################################
# Fungsi Bawaan
#1. bool(): Mengonversi nilai atau ekspresi ke tipe data boolean.
angka = 42
status = bool(angka > 50)
print(status)  # Output: False

#2. and, or, dan not: Operator logika untuk menggabungkan atau membalikkan kondisi boolean.
kondisi_1 = True
kondisi_2 = False

hasil_and = kondisi_1 and kondisi_2
hasil_or = kondisi_1 or kondisi_2
hasil_not = not kondisi_1

print(hasil_and)  # Output: False
print(hasil_or)   # Output: True
print(hasil_not)  # Output: False

#3. all(): Mengembalikan True jika semua elemen dalam suatu iterable adalah True.
list_boolean = [True, True, False, True]
hasil_all = all(list_boolean)
print(hasil_all)  # Output: False

#4. any(): Mengembalikan True jika setidaknya satu elemen dalam suatu iterable adalah True.
list_boolean = [False, False, True, False]
hasil_any = any(list_boolean)
print(hasil_any)  # Output: True

#5. is dan is not: Operator identitas untuk memeriksa apakah dua objek adalah sama atau tidak.
x = True
y = True
z = False

print(x is y)      # Output: True
print(x is not z)  # Output: True

#6. == dan !=: Operator perbandingan untuk memeriksa kesamaan atau ketidak-samaan antara dua nilai.
a = True
b = False

print(a == b)  # Output: False
print(a != b)  # Output: True
