# membuat set
buah_set = {"apel", "mangga", "pisang", "apel"}
print(buah_set) # output >>> {'pisang', 'apel', 'mangga'}
print(type(buah_set)) # output >>> <class 'set'>

# menambah elemen ke dalam set
buah_set.add("jeruk")
print(buah_set) # output >>> {'pisang', 'apel', 'mangga', 'jeruk'}

# menghapus elemen dari set
buah_set.remove("mangga")
print(buah_set) # output >>> {'jeruk', 'apel', 'pisang'}

# operasi himpunan
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}

gabungan = set_1.union(set_2)
irisan = set_1.intersection(set_2)
selisih = set_1.difference(set_2)

print(gabungan) # output >>> {1, 2, 3, 4, 5, 6}
print(irisan) # output >>> {3, 4}
print(selisih) # output >>> {1, 2}

# iterasi
for buah in buah_set:
    print(buah)

# output >>>
# jeruk
# apel
# pisang

# nilai 'true' dan '1' dianggap sama, begitupun 'false' dan '0'
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # output >>> {True, 2, 'banana', 'apple', 'cherry'}

# mengetahui panjang set
print(len(thisset)) # output >>> 5

# merubah array menjadi set
set_list = set(("apple", "banana", "cherry")) # gunakan kurung dobel
print(set_list) # output >>> {'cherry', 'banana', 'apple'}

#################################
# Fungsi Bawaan
#1. len(): Mengembalikan jumlah elemen dalam set.
my_set = {1, 2, 3, 4, 5}
panjang_set = len(my_set)
print(panjang_set)  # Output: 5
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

#2. add(): Menambahkan elemen ke dalam set.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

#3. update(): Menambahkan elemen-elemen dari suatu iterable (seperti set atau list) ke dalam set.
set_pertama = {1, 2, 3}
set_kedua = {3, 4, 5}
set_pertama.update(set_kedua)
print(set_pertama)  # Output: {1, 2, 3, 4, 5}

#4. remove() dan discard(): Menghapus elemen tertentu dari set. Perbedaannya, jika elemen tidak ada, remove() akan menghasilkan KeyError, sementara discard() tidak menghasilkan error.
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

#5. pop(): Menghapus dan mengembalikan elemen acak dari set.
my_set = {1, 2, 3, 4, 5}
elemen_terhapus = my_set.pop()
print(my_set)         # Output: Set dengan satu elemen kurang dari sebelumnya
print(elemen_terhapus)  # Output: Elemen yang terhapus

#6. clear(): Menghapus semua elemen dari set, membuat set menjadi kosong.
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)  # Output: set()

#7. union() atau |: Menggabungkan dua set, menghasilkan set baru yang berisi semua elemen dari kedua set.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_gabungan = set_a.union(set_b)
print(set_gabungan)  # Output: {1, 2, 3, 4, 5}

#8. intersection() atau &: Menghasilkan set yang berisi elemen-elemen yang ada di kedua set.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_irisan = set_a.intersection(set_b)
print(set_irisan)  # Output: {3, 4}

#9. difference() atau -: Menghasilkan set yang berisi elemen-elemen yang ada di set pertama tetapi tidak ada di set kedua.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_selisih = set_a.difference(set_b)
print(set_selisih)  # Output: {1, 2}

#10. symmetric_difference() atau ^: Menghasilkan set yang berisi elemen-elemen yang hanya ada di salah satu dari kedua set.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_dif_simetris = set_a.symmetric_difference(set_b)
print(set_dif_simetris)  # Output: {1, 2, 5, 6}
