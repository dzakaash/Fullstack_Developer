#soal 1, mencari selisih maksimum dan minimum
def selisih_max(data):
    if not data:
        return None
    max = min = data[0]
    for angka in data:
        if angka > max:
            max = angka
        elif angka < min:
            min = angka
    selisih = max - min
    return selisih

list1 = [10, 15, 20, 2, 10, 6]
hasil_selisih = selisih_max(list1)
print(hasil_selisih)
    
# # output >>> 18 

# #soal 3, mencari number terkecil
def angka_min(data):
    if not data:
        return None
    minimum = data[0]
    for angka in data:
        if angka < minimum:
            minimum = angka

    return minimum

list2 = [34, 15, 88, 2]
minimum = angka_min(list2)
print(minimum)

# # output >>> Angka terkecil dari list [34, 15, 88, 2] adalah: 2

#soal 4, mengembalikan nilai pertama dan terakhir
def awal_akhir(data):
    if not data:
        return None
    awal = data[0]
    akhir = data[-1]
    hasil = [awal, akhir]
    
    return hasil

awal_akhir1 = awal_akhir([5, 10, 15, 20, 25])
print(awal_akhir1)
# output >>> [5, 25]

# #Soal 5, mengecek keberadaan dalam list
def cek_list(data, cari):
    return cari in data

cek1 = cek_list([1, 2, 3, 4, 5], 3)
print(cek1)
# # output >>> True

def cek_list(data, cari): # definisikan fungsi
    hasil = False # hasil bernilai false pertama-tama
    for angka in data: # isi list disebut angka
        if angka == cari: # jika angka sama dengan yang dicari hasilnya True
            hasil = True
            break #menghentikan looping setelah terpenuhi True
        else: # jika tidak serupa maka anggap False, namun ini tidak perlu jika sudah ada break dan hasil sudah dianggap False
            hasil = False
    return hasil # return hasilnya

cek1 = cek_list([1, 2, 3, 4, 5], 3)
print(cek1)

#Soal 6, invert list
def invertList(data):
    invert_list = []
    index = 0
    while index < len(data):
        index += 1
    while index > 0:
        index -= 1
        invert_list.append(-data[index])
    return invert_list

invert1 = invertList([1, 2, 3, 4, 5])
print(invert1)
# # output >>> [-5, -4, -3, -2, -1]

#Soal 7, convert ke string
def list_string(data):
    list_string = []
    for elemen in data:
        if type(elemen) == int:
            elemen = str(elemen)
        list_string.append(elemen)
    return list_string

listString1 = list_string([1, 2, "a", "b"])
print(listString1)
# # output >>> ['1', '2', 'a', 'b']

#Soal 8, menemukan indeks
def temukan_indeks(data, elemen):
    for i in range(len(data)):
        if data[i] == elemen:
            return i
    return -1

indeks1 = temukan_indeks(["hi", "edabit", "fgh", "abc"], "fgh")
print(indeks1)
# # output >>> 2