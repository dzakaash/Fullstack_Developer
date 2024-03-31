angka = [1, 2, 3, 4, 5] #list berisi integer
buah = ["Apel", "Jeruk", "Pisang", "Mangga"] #list berisi string
campuran = [1, "dua", 3.0, True] #list berisi campuran
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #list dalam list, disebut list 2 dimensi

print(angka)
print(buah)
print(campuran)

#cek tipe
print(type(angka))
print(type(buah))
print(type(campuran))
print(type(nested_list))

print(buah[0]) #memilih berdasarkan indeks
print(buah[1:3]) #melakukan slicing

angka2 = [6, 7, 8, 9, 10]
angka_gabungan = angka + angka2 #melakukan penggabungan
print (angka_gabungan)

ulang_buah = buah*3 #melakukan pengulangan
print(ulang_buah)

panjang_ag = angka_gabungan.__len__() #mengetahui panjang
print(panjang_ag)
print(len(angka_gabungan)) #print langsung panjang list

kota = ("Jakarta", "Bandung", "Surabaya", "Yogyakarta")
list_kota = list(kota) #mengubah menjadi list
print(list_kota)

#menyisipkan elemen
angka_tambahan = angka.insert(1, 2.5)
print(angka_tambahan)

#menghapus elemen
buah_favorit = buah.pop("Mangga")
print(buah_favorit)

#menambah elemen di akhir
angka3 = angka.append(6) 
print(angka3)

####################################
# Fungsi Bawaan
#1. len(): Mengembalikan panjang (jumlah elemen) dari suatu list.
my_list = [1, 2, 3, 4, 5]
panjang_list = len(my_list)
print(panjang_list)  # Output: 5
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

#2. append(): Menambahkan elemen ke akhir list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
# Tanpa menggunakan fungsi bawaan append()
list_angka = [1, 2, 3] # Langkah 1: Inisialisasi list angka
nilai_tambahan = 4 # Langkah 2: Inisialisasi nilai yang akan ditambahkan
list_angka_manual = list_angka + [nilai_tambahan] # Langkah 3: Menggunakan operasi concatenation (+) untuk menambahkan nilai ke list
print(f"List setelah penambahan manual: {list_angka_manual}") # Output: "List setelah penambahan manual: [1, 2, 3, 4]"

#3. : extend(): Menambahkan elemen-elemen dari suatu iterable (seperti list) ke akhir list.
list_pertama = [1, 2, 3]
list_kedua = [4, 5, 6]
list_pertama.extend(list_kedua)
print(list_pertama)  # Output: [1, 2, 3, 4, 5, 6]
# Tanpa menggunakan fungsi bawaan extend()
list_angka = [1, 2, 3] # Langkah 1: Inisialisasi list angka
iterable_tambahan = [4, 5, 6] # Langkah 2: Inisialisasi iterable yang akan ditambahkan
for elemen in iterable_tambahan: # Langkah 3: Menggunakan loop untuk menambahkan setiap elemen dari iterable
    list_angka.append(elemen)
print(f"List setelah penambahan manual: {list_angka}") # Output: "List setelah penambahan manual: [1, 2, 3, 4, 5, 6]"

#4. insert(): Menyisipkan elemen pada indeks tertentu.
my_list = [1, 2, 3, 5]
my_list.insert(3, 4)
print(my_list)  # Output: [1, 2, 3, 4, 5]
# Tanpa menggunakan fungsi bawaan insert()
list_angka = [1, 2, 3] # Langkah 1: Inisialisasi list angka
indeks_tujuan = 1 # Langkah 2: Inisialisasi indeks di mana elemen akan dimasukkan
nilai_tambahan = 4 # Langkah 3: Inisialisasi nilai yang akan dimasukkan
bagian_awal = list_angka[:indeks_tujuan] # Langkah 4: Pecah list menjadi dua bagian di indeks yang dituju
bagian_akhir = list_angka[indeks_tujuan:]
list_angka_manual = bagian_awal + [nilai_tambahan] + bagian_akhir # Langkah 5: Gabungkan bagian awal, nilai tambahan, dan bagian akhir menjadi list baru
print(f"List setelah penambahan manual: {list_angka_manual}") # Output: "List setelah penambahan manual: [1, 4, 2, 3]"

#5. remove(): Menghapus elemen tertentu dari list.
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]
# Tanpa menggunakan fungsi bawaan remove()
list_angka = [1, 2, 3, 2, 4] # Langkah 1: Inisialisasi list angka
nilai_hapus = 2 # Langkah 2: Inisialisasi nilai yang akan dihapus
indeks_hapus = None # Langkah 3: Mencari indeks pertama dari nilai yang akan dihapus
for i in range(len(list_angka)):
    if list_angka[i] == nilai_hapus:
        indeks_hapus = i
        break
if indeks_hapus is not None: # Langkah 4: Hapus nilai jika ditemukan
    list_angka_manual = list_angka[:indeks_hapus] + list_angka[indeks_hapus + 1:]
else:
    list_angka_manual = list_angka[:]
print(f"List setelah penghapusan manual: {list_angka_manual}") # Output: "List setelah penghapusan manual: [1, 3, 2, 4]"

#6. pop(): Menghapus dan mengembalikan elemen pada indeks tertentu atau indeks terakhir jika tidak diindikasikan.
my_list = [1, 2, 3, 4, 5]
elemen_terhapus = my_list.pop(2)
print(my_list)         # Output: [1, 2, 4, 5]
print(elemen_terhapus)  # Output: 3
# Tanpa menggunakan fungsi bawaan pop()
list_angka = [1, 2, 3, 4] # Langkah 1: Inisialisasi list angka
indeks_pop = 2 # Langkah 2: Inisialisasi indeks yang akan di-pop
elemen_di_pop_manual = list_angka[indeks_pop] # Langkah 3: Ambil elemen pada indeks yang akan di-pop
list_angka_manual = list_angka[:indeks_pop] + list_angka[indeks_pop + 1:] # Langkah 4: Hapus elemen pada indeks yang akan di-pop
print(f"List setelah menggunakan pop manual: {list_angka_manual}") # Langkah 5: Tampilkan hasil
print(f"Elemen yang di-pop manual: {elemen_di_pop_manual}")
# Output: "List setelah menggunakan pop manual: [1, 2, 4]"
#         "Elemen yang di-pop manual: 3"

#7. index(): Mengembalikan indeks dari elemen pertama dengan nilai tertentu.
my_list = [10, 20, 30, 20, 40]
indeks = my_list.index(20)
print(indeks)  # Output: 1
# Tanpa menggunakan fungsi bawaan index()
list_angka = [1, 2, 3, 4] # Langkah 1: Inisialisasi list angka
elemen_dicari = 3 # Langkah 2: Inisialisasi elemen yang dicari
indeks_tiga_manual = None # Langkah 3: Loop untuk mencari indeks pertama dari elemen
for i in range(len(list_angka)):
    if list_angka[i] == elemen_dicari:
        indeks_tiga_manual = i
        break
if indeks_tiga_manual is not None: # Langkah 4: Tampilkan hasil
    print(f"Indeks dari elemen {elemen_dicari} manual: {indeks_tiga_manual}")
else:
    print(f"Elemen {elemen_dicari} tidak ditemukan dalam list.") # Output: "Indeks dari elemen 3 manual: 2"

#8. count(): Menghitung berapa kali suatu nilai muncul dalam list.
my_list = [1, 2, 3, 2, 4, 2, 5]
jumlah_dua = my_list.count(2)
print(jumlah_dua)  # Output: 3
# Tanpa menggunakan fungsi bawaan count()
list_angka = [1, 2, 3, 2, 4, 2] # Langkah 1: Inisialisasi list angka
elemen_diitung = 2 # Langkah 2: Inisialisasi elemen yang akan dihitung
jumlah_dua_manual = 0 # Langkah 3: Hitung jumlah kemunculan elemen secara manual
for elemen in list_angka:
    if elemen == elemen_diitung:
        jumlah_dua_manual += 1
print(f"Jumlah kemunculan elemen {elemen_diitung} manual: {jumlah_dua_manual}") # Output: "Jumlah kemunculan elemen 2 manual: 3"

#9. sort(): Mengurutkan elemen dalam list.
my_list = [4, 2, 1, 3]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]
# Tanpa menggunakan fungsi bawaan sort()
list_angka = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] # Langkah 1: Inisialisasi list angka
n = len(list_angka) # Langkah 2: Algoritma Bubble Sort secara manual
for i in range(n):
    for j in range(0, n-i-1):
        if list_angka[j] > list_angka[j+1]:
            # Tukar elemen jika tidak terurut
            list_angka[j], list_angka[j+1] = list_angka[j+1], list_angka[j]
print(f"List setelah pengurutan manual: {list_angka}") # Output: "List setelah pengurutan manual: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]"

#10. reverse(): Membalik urutan elemen dalam list.
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]
# Tanpa menggunakan fungsi bawaan reverse()
list_angka = [1, 2, 3, 4, 5] # Langkah 1: Inisialisasi list angka
# Langkah 2: Algoritma untuk membalik list secara manual
# Kita dapat menggunakan teknik slicing untuk membalik list
list_angka_manual = list_angka[::-1]
print(f"List setelah pembalikan manual: {list_angka_manual}")
# Output: "List setelah pembalikan manual: [5, 4, 3, 2, 1]"
