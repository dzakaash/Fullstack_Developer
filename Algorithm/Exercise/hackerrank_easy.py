# # No.1 Simply Array Sum, https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
# def simpleArraySum(ar):
#     # Write your code here
#     sum = 0
#     for num in ar:
#         sum += num
#     return sum

# # No. 2 Compare the Triplets, https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
# def compareTriplets(a, b):
#     alice_point = 0
#     bob_point = 0
#     i = 0
#     while i < len(a):
#         if a[i] > b[i]:
#             alice_point +=1
#         elif a[i] < b[i]:
#             bob_point +=1
#         i +=1
#     return [alice_point, bob_point]
# print(compareTriplets([5, 6, 7], [3, 6, 10]))
# print(compareTriplets([17, 28, 30], [99, 16, 8]))

# # No.3 A Very Big Sum, https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true
# def aVeryBigSum(ar):
#     sum = 0
#     i = 0
#     while i < len(ar):
#         sum += ar[i]
#         i +=1
#     return sum
# print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

# # No. 4 Diagona Difference, https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

# def diagonalDifference(arr):
#     d1 = 0
#     d2 = 0
#     for i in range(len(arr)):
#         d1 += arr[i][i]
#         d2 += arr[i][len(arr)-i-1]
#     result = d1-d2
#     return abs(result)
# print(diagonalDifference([
#                         [11, 2,   4],
#                         [4,  5,   6],
#                         [10, 8, -12]]))

# No. 5 Plus Minus, https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
# def plusMinus(arr):
#     plus = 0
#     minus = 0
#     zero = 0
#     total = len(arr)

#     for num in arr:
#         if num > 0:
#             plus += 1
#         elif num < 0:
#             minus += 1
#         else:
#             zero += 1

#     # Mencetak hasil dengan format yang benar
#     print("{:.6f}".format(plus / total)) # ":.6f".format(angka) untuk menampilkan 6 digit di belakang koma 
#     print("{:.6f}".format(minus / total))
#     print("{:.6f}".format(zero / total))

# # Mencetak hasil dari fungsi plusMinus
# plusMinus([-4, 3, -9, 0, 4, 1])


# # NO. 6 Staircase, https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
# def staircase(n):
#     space = n-1
#     hastag = 1
#     while hastag <= n:
#         print(" " * space + "#" * hastag)
#         space -= 1
#         hastag += 1
# staircase(6)

# # No. 7 Mini Max Sum, https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
# def miniMaxSum(arr):
#     maximum = sorted(arr, reverse=True)
#     minimum = sorted(arr)
#     sum_max = sum(maximum) - maximum[-1]
#     sum_min = sum(minimum) - minimum[-1]
#     print(sum_min, sum_max)
# miniMaxSum([1, 2, 3, 4, 5])

# # No. 8 Birthday Cake Candles, https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
# def birthdayCakeCandles(candles):
#     num_max = max(candles)
#     count = 0
#     for num in candles:
#         if num == num_max:
#             count +=1
#     return count
# print(birthdayCakeCandles([3, 2, 1, 3]))

# # No. 9 Time Conversion, https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
# def timeConversion(s):
#     clock = int(s[:2])
#     if "A" in s: # pisahkan untuk AM
#         if clock >=12: #jika lebih besar dari 12, maka AM akan ulang dari 0
#             while clock >=12: 
#                 clock -= 12 # kurangi terus 12 selama lebih dari 12
#                 if clock < 10: # jika kurang dari 10, maka hanya ada satu digit, maka harus ditambah 0 di depan
#                     time = "0" + str(clock) + s[2:8]
#                 elif clock >= 10: #jika lebih sama dengan 10 maka sudah pas 2 digit
#                     time = str(clock) + s[2:8]
#         else : # yang lainnya jika sudah sejak awal kurang dari 12, bisa langsung lakukan operasi yang sama seperti diatas
#             if clock < 10:
#                     time = "0" + str(clock) + s[2:8]
#             elif clock >= 10:
#                 time = str(clock) + s[2:8]
#     elif "P" in s: # pisahkan untuk PM
#         if clock >= 24: #jika lebih besar dari 24, maka PM harus kurang dari 24, namun kita akan buat kembali lebih dari 12
#             while clock >= 24:
#                 clock -= 24
#                 if clock < 12: # kita buat yang kurang dari jam 12, lebih dari 12 karena PM artinya lewat dari jam 12 pagi
#                     clock +=12
#                     time = str(clock) + s[2:8]
#                 else: # yang lainnya jika sudah lebih dari 12, maka sudah sesuai menunjukkan waktu lewat jam 12 pagi
#                     time = str(clock) + s[2:8]
#         if clock < 12: # sama seperti operasi diatas, kita akan buat lebih dari jam 12 pagi
#             clock += 12
#             time = str(clock) + s[2:8]
#         else: # yang lainnya sejak awal sudah sesuai menunjukkan waktu lewat jam 12 pagi
#             time = str(clock) + s[2:8]
#     return time
# print(timeConversion("07:05:45AM"))

#No. 10 Grading Studets, https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
# def gradingStudents(grades):
#     # Write your code here
#     for i in range(len(grades)):
#         if grades[i] >= 38 :
#             mod = grades[i]%5
#             if mod>2 :
#                 grades[i] = grades[i] + 5 - mod
#     return grades 
# print(gradingStudents([4, 73, 67, 38, 33]))
# print(gradingStudents([2, 37, 38]))
# print(gradingStudents([23, 80, 96, 18, 73, 78, 60, 60, 15, 45, 15, 10, 5, 46, 87, 33, 60, 14, 71, 65, 2, 5, 97, 0]))
# print(gradingStudents([44, 84, 94, 21, 0, 18, 100, 18, 62, 30, 61, 53, 0, 43, 2, 29, 53, 61, 40, 14, 4, 29, 98, 37, 23, 46, 9, 79, 62, 20, 38, 51, 99, 59, 47, 4, 86, 61, 68, 17, 45, 6, 1, 95, 95]))

#no. 11 Apples and Oranges, https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     apple_house = 0
#     orange_house = 0
#     for apple in apples:
#         if apple + a >= s and apple + a <= t:
#             apple_house += 1
#     for orange in oranges:
#         if orange + b >= s and orange + b <= t:
#             orange_house += 1
#     print(apple_house)
#     print(orange_house)
# countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

#No. 12 Kangaroo, https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# def kangaroo(x1, v1, x2, v2):
#     jump1 = x1
#     jump2 = x2
#     if x1 == x2:
#         return "NO"
#     elif x1 < x2 and v1 < v2:
#         return "NO"
#     elif x2 < x1 and x2 < v1:
#         return "NO" 
#     else:
#         if v1 > v2:    
#             while jump1 <= jump2:
#                 jump1 += v1
#                 jump2 += v2
#                 if jump1 == jump2:
#                     return "YES"
#         elif v2 > v1:
#             while jump2 <= jump1:
#                 jump1 += v1
#                 jump2 += v2
#                 if jump1 == jump2:
#                     return "YES"
#     return "NO"
# print(kangaroo(21, 6, 47, 3))

#No.13 Get Total, https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
# def getTotalX(a, b):
#     max_a = max(a)
#     min_b = min(b)
#     max_b = max(b)
#     c = [] # wadah calon faktorial
#     d = [] # wadah final faktorial
#     # buat agar kita dapat kelipatan dari bilangan di a yang tidak ada di a dan tidak melebihi b
#     for i in a:
#         i_fact = 0
#         while i_fact < min_b:
#             i_fact += i
#             c.append(i_fact)
#     for j in c:  # untuk setiap bilangan di c kita akan cek faktorialnya
#         for k in range(j, max_b, j): # untuk faktorial dari j, maka kita cek
#             if k in b: # apakah ada k yang di b? 
#                 d.append(j) # jika ada, maka kita masukkan bilangan dari c itu ke d
#     # kita lakukan perhituangan jumlah faktorialnya
#     count = 0
#     e = []
#     for l in d:
#         if l >= max_a:
#             if l not in e:
#                 e.append(l)
#                 count += 1
#     return count
# def getTotalX(a, b):
#     # Mencari rentang dari nilai minimum dalam a hingga maksimum dalam b
#     min_a = min(a)
#     max_b = max(b)
    
#     # Menghitung jumlah bilangan yang memenuhi syarat
#     count = 0
#     for num in range(min_a, max_b + 1):
#         if all(num % factor == 0 for factor in a) and all(b_num % num == 0 for b_num in b):
#             count += 1
    
#     return count

# # Contoh penggunaan fungsi dengan input yang diberikan
# print(getTotalX([2, 4], [16, 32, 96]))  # Output: 3
# print(getTotalX([2], [20, 30, 12]))     # Output: 1
# print(getTotalX([3, 9, 6], [36, 72]))   # 

# No. 14 Breaking Records, https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
# def breakingRecords(scores):
#     max = min = scores[0]
#     count_max = 0
#     count_min = 0
#     for num in scores:
#         if num > max:
#             max = num
#             count_max += 1
#         if num < min:
#             min = num
#             count_min += 1
#     return [count_max, count_min]

# print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))

# No. 15 The Birthday Bar, https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
# def birthday(s, d, m):
#     ron = 0 #perhitungan cara pembagian coklat, sudah diawali 0
#     i = 0 # untuk indeks pembatas looping while
#     while i < len(s) - m + 1: # selama indeksnya kurang dari panjang s, bakal terus ngelooping
#         sum = 0 # ini untuk jumlah integernya, biar disamakan dengan d, jadi bakal mulai dar 0 lagi saat mulai indeks baru
#         long_cho = 0 # ini panjang coklatnya, jadi pembatas looping penambahan ke sum, kalau panjangnya udah pas
#         j = i
#         while long_cho < m: # kita looping selama panjang coklatnya tidak melebihi m
#             sum += s[j] # kita tambahkan sum dengan elemen dari s itu
#             long_cho += 1 # kita tambahkan long_cho dengan 1 agar tau udah berapa panjang
#             j += 1 # kita tambakan j dengan satu agar kita mulai dengan coklat selanjutnya
#         if sum == d: #jika hasil loopingan diatas ada yang sama nilainya dengan d, maka
#             ron += 1 # ron bakal ditambah 1
#         i += 1 # kita mulai lagi dengan baris berikutnya
#     return ron 
# print(birthday([1, 2, 1, 3, 2], 3, 2)) #2
# print(birthday([1, 1, 1, 1, 1, 1], 3, 2)) #0
# print(birthday([4], 4, 1)) #1
# print(birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7)) #3

# No. 16 Divisible Sum Pairs, https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
# def divisibleSumPairs(n, k, ar):
#     count_pairs = 0 # untuk perhitungan pasangannya
#     i = 0
#     while i < n: # kita akan looping untuk mengecek setiap elemen, selama indeksnya tidak melebihi n 
#         j = 0
#         while j < n:
#             if i < j and (ar[i] + ar[j]) % k == 0:
#                count_pairs +=1
#             j += 1
#         i += 1
#     return count_pairs 
# print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))

# No. 17 Migratory Birds, https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
# def migratoryBirds(arr):
#     bird_max = arr[0] # kita anggap bird max adalah bird pertama
#     count_max = 0 # kita anggap angka maksimal masih 0
#     birds = [1, 2, 3, 4, 5]
#     for bird in birds : # kita akan loop tiap jenis burung, berapa banyak muncul burung yang sama
#         count = 0 #  hitungan untuk burung tertentu itu disini
#         i = 0 # index untuk burung mengecek burung mulai dari nol
#         while i < len(arr): #kita akan cek tiap masing-masing burung
#             if arr[i] == bird: #jika burung itu bernilai sama dengan burung yang kita samakan
#                 count +=1 #maka perhitungan untuk burung itu ditambah satu
#             i += 1 # index nya tambah satu untuk bandingkan dengan burung selanjutnya
#         if count > count_max: 
#             bird_max = bird
#             count_max = count
#         elif count == count_max and bird < bird_max:
#             bird_max = bird
#     return bird_max
# print(migratoryBirds([1, 4, 4, 4, 5, 3]))
# print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))

# No. 18 Day of The Programmer, https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
# hari pemrograman adalah hari ke 256, cari dalam format dd.mm.yyyy
# tahun antara 1700 - 2700, tahunnya dalam y
# tahun 1700 - 1917 kalender resmi Rusia julian
# tahun 1918 kalendernya berubah jadi gregorian
# berpindah dari 01 Februari 1918 Julian langsung ke 14 Februari 1918 Gregorian
# Baik Julian atau Gregorian, Februari akan 29 hari pada kabisat, dan 28 hari di tahun biasa
# Dalam kalender Julian tahun kabisat habis dibagi 4
# Dalam kalender Gregorain tahun kabisat habis dibagi 400, 4, dan tidak habis dibagi 100
# Jawaban ada tiga, antara 12.09 jika di tahun biasa, 13.09 di tahun kabisat
# def dayOfProgrammer(year):
#     if year == 1918:
#         return "26.09.1918"
#     elif year < 1918:
#         if year % 4 == 0:
#             return "12.09." + str(year)
#         else:
#             return "13.09." + str(year)
#     else:
#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             return "12.09." + str(year)
#         else:
#             return "13.09." + str(year)
# print(dayOfProgrammer(2017))
# print(dayOfProgrammer(2016))
# print(dayOfProgrammer(1700))
# print(dayOfProgrammer(1900))
# print(dayOfProgrammer(1800))

# No. 19 Bon Appetite, https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
# biaya yang dibagi dua hanya yang dimakan saja
# kalau dibagi secara adil jawab "Bon Appetit", jika tidak maka kembalikan jumlah kembalian bilangan bulat
# def bonAppetit(bill, k, b):
#     total = sum(bill) - bill[k]
#     split = int(total/2)
#     if split == b: # jika split itu sama nilainya dengan b, maka kita kembalikan bon appetit
#         return print("Bon Appetit")
#     elif split != b: # jika tidak maka kembaliannya
#         return print(b - split)
# print(bonAppetit([3, 10, 2, 9], 1, 12)) #5
# print(bonAppetit([3, 10, 2, 9], 1, 7)) #Bon Appetit

# No. 20 Sock Merchant, https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
# def sockMerchant(n, ar):
#     pairs = 0 # ini tempat perhitungan pasangan kaos kaki
#     ar.sort() # kita urutkan saja langsung
#     i = 0 # indeks untuk batas perulangan
#     while i < n-1:
#         if ar[i] == ar[i+1]:
#             pairs += 1
#             i += 1
#         i += 1
#     return pairs
# print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])) #3
# print(sockMerchant(15, [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5])) #6

# No. 21 Drawing Book, https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
# guru meminta untuk membuka halaman buku ke nomor tertentu
# buku bisa dibuka dari depan atau belakang
# mereka membaliknya selalu satu per satu
# saat dibuka, maka halaman 1 selalu ada di kanan
# setiap halaman kecuali halaman terakhir akan selalu dicetap pada kedua sisi
# halaman terakhir hanya boleh dicetak bagian depannya saja, mengingat panjang bukunya
# panjang buku dalam n halaman
# halaman yang ingin di buka dalam p
# kita harus mencari jumlah minimum halaman yang harus dibalik, bisa dari depan atau belakang
# def pageCount(n, p):
#     flip_front = p // 2 # dengan membaginya langsung dengan 2 dengn dibulat kebawah, maka jika menghitung dari depan kita sudah bisa dapat berapa flipnya 
#     # untuk menghitung dari belakang ada dua keadaan
#     if n % 2 == 0:  # jika halamannya genap
#         flip_back = (n - p + 1) // 2 # maka banyak balikan adalah banyak halaman ditambah 1 - halaman yang dicari, ditambah satu agar halaman terakhir ada pasangannya
#     else:  # Jika halamaanya ganjil
#         flip_back = (n - p) // 2
#     return min(flip_front, flip_back) #cukup pakai min untuk bandingkan mana yang terkecil
# print(pageCount(6, 2)) #1
# print(pageCount(5, 4)) #0

# No. 22 Counting Valleys, https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
# def countingValleys(steps, path):
#     sea_level = 0
#     valley = 0
#     for step in path:
#         if step == "D":
#             sea_level -= 1
#         elif step == "U":
#             sea_level += 1
#             if sea_level == 0:
#                 valley +=1
#     return valley
        
# No. 23 Electronics Shop, https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
# def getMoneySpent(keyboards, drives, b):
#     bill = []
#     for keyboard in keyboards:
#         for drive in drives:
#             if keyboard + drive <= b:
#                 bill.append(keyboard+drive)
#     if len(bill) == 0:
#         return -1
#     else:
#         return max(bill)

# # No. 24 Cats and Mouse, https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
# def catAndMouse(x, y, z):
#     if abs(z-x) < abs(y-z):
#         return "Cat A"
#     elif abs(z-x) > abs(y-z):
#         return "Cat B"
#     else:
#         return "Mouse C"


# 26. Picking Numbers, https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
# pertama-tama kita ururtkan dahulu
# setelah itu kita atur jika ada elemen yang sama atau selisihnya kurang dari satu, masukan ke sebuah array
# berarti kita harus buat array baru terus??? mungkin cukup angkanya saja, terus bandingkan
# yang pasti kita akan bandingkan mana array terpanjang
# def pickingNumbers(a):
#     a.sort() #kita urutkan dahulu, kayaknya gk diurutkan juga tidak apa
#     length = 0 #setelah itu kita buat awalan panjangnya, 0 dulu
#     for i in a: # kita akan coba bandingkan salah satu elemen dengan semua elemen di array
#         length_try = 0 #panjang dari elemen di array dengan item itu kita catat disini
#         for j in a: # ini elemen yang kita bandingkan dengan elemen itu
#             if i <= j and j - i <= 1: #kalau ternyata kurang dari sama dengan satu selisihnya, kita batasi j harus lebih besar agar tidak terbawa dua jenis nomor
#                 length_try += 1 #tambah satu panjangnya
#         if length_try > length: #sebelum bubar, kita bandingkan dulu mana yang paling panjang
#             length = length_try #kalau lebih panjang, maka akan jadi panjang yang baru
#     return length
# print(pickingNumbers([4, 6, 5, 3, 3, 1]))

# #No. 28. The Hurdle Race, https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
# # cari berapa dosis ramuan agar bisa melewati semua rintangan
# def hurdleRace(k, height):
#     max_height = max(height)
#     if max_height > k:
#         doses = max_height - k
#     else :
#         doses = 0
#     return doses
    
#No. 29 Designer PDF Viewer, https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
# diberikan list tinggi huruf dari a-z
# hitung luas highlight jika semuanya lebarnya sama yaitu 1
# def designerPdfViewer(h, word):
#     letters = "abcdefghijklmnopqrstuvwxyz"
#     height_max = 0
#     idx = 0
#     while idx < len(word):
#         jdx = 0
#         while jdx < len(letters):
#             if word[idx] == letters[jdx]:
#                 height = int(h[jdx])
#                 if height > height_max:
#                     height_max = height
#             jdx += 1
#         idx += 1
#     highlight = height_max * len(word)
#     return highlight
# print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], "abc")) #9

#No. 30 Utopian Tree, https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
# ada dua siklus pertumbuan, ketika musim semi 2 kali lipat, dan musim panas bertambah 1 meter
# anakan pohon ditanam awal musim semi
# def utopianTree(n):
#     height = 0
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             height += 1
#         else:
#             height *= 2
#         i += 1
#     return height
# print(utopianTree(0)) #1
# print(utopianTree(1)) #2
# print(utopianTree(4)) #7

#No. 31 Angry Profesor, https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true
# def angryProfessor(k, a):
#     line = 0 #kita buat variabel untuk perhitungan
#     for student in a: #kita mulai looping untuk periksa satu-satu kalau ada yang kurang sama dengan 0, yang artinya datang tepat wktu
#         if student <= 0:
#             line += 1 #nah, kalau ada, berarti perhitungan tambah 1
#     if line >= k: #kalau pehitungan lebih sama dengan batas, maka lolos
#         return "NO" #kelas tidak dibatalkan
#     else:
#         return "YES" #kalau yang hadir kurang maka kelas dibatalkan
# print(angryProfessor(3, [-1, -3, 4, 2])) #"YES"
# print(angryProfessor(2, [0, -1, 2, 1])) #"NO"
# print(angryProfessor(20, [97, -55, 48, -22, 99, -46, 40, 11, 5, -61, 78, -20, 44, 22, -8, 82, 24, -62, 0, 52, -79, 68, -73, -81, 33, 60, -99, -99, 59, -13, 90, -26, 84, 90, 76, 36, -45, 79, 87, 48, 59, -36, 42, -6, -13, 21, -19, -21, 39, -40])) #"NO"

# #No. 32 Beautiful Days, https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
# def beautifulDays(i, j, k):
#     beautiful_day = 0
#     days = set(range(i, j+1))
#     for day in days:
#         print("day", day)
#         string_day = str(day)
#         rvrs_day = string_day[::-1] #gunakan slice [::-1] untuk membalik string, dimana rentangnya berupa bilangan negatif
#         int_rvrs_day = int(rvrs_day)
#         if abs(day - int_rvrs_day) % k == 0:
#             beautiful_day += 1
#     return beautiful_day
# print(beautifulDays(20, 23, 6))

#No. 33 Viral Advertising, https://www.hackerrank.com/domains/algorithms?badge_type=problem-solving
# def viralAdvertising(n):
#     share = 5 #share awal 5 orang
#     days = 1 #hari pertama 1
#     cummulative = 0 #cummulative pertama 2
#     while days < n+1: #while loop selama kurang dari hari yang dicari
#         share_new = (share // 2) * 3 #ini perhitungan share baru
#         cummulative += (share // 2)
#         share = share_new #share baru
#         days += 1
#     return cummulative
# print(viralAdvertising(3)) #9

#No. 34 Save The Prisoner, https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true
#tahanan dan sejumlah hadiah untuk dibagikan
#membagikan cemilan dengan mendudukkan para tahanan di sekeliling meja bundar di kursi yang diberi nomor urut
#permen dibagikan berdasarkan nomor kursi yang telah diambil dari topi, secara berkeliling
#permen terakhir adalah permen yang rasanya tidak enak, cari nomor kursi yang dapat permen itu

# def saveThePrisoner(n, m, s):
#     # candy = ((m % n) + s - 1) % n
#     # if candy > 0:
#     #     reminder = candy
#     # elif candy == 0:
#     #     reminder = n
#     # return reminder
#     x=((m-1)%n)+s
#     if x>n:
#         x-=n
  
#     return x 
# print(saveThePrisoner(4, 6, 2)) #3
# print(saveThePrisoner(5, 2, 1)) #2
# print(saveThePrisoner(5, 2, 2)) #3
# print(saveThePrisoner(5, 5, 1)) #5
# print(saveThePrisoner(352926151, 380324688, 94730870)) #122129406

#No. 35 Circular Array Rotation, https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true
# rotasi melingkar ke kanan untuk array berisi blangan bulat
# saat digeser ke kanan, maka array terakhir berpindah ke posisi pertama
# a = array, k = jumlah putaran, queries = indeks yang dikembalikan 
# def circularArrayRotation(a, k, queries):
#     new_array = []
#     for que in queries:
#         new_array.append(a[(que - k) % len(a)]) #indeks baru cukup dari indeks yang diepsan kurangi pertambahan, agar kita kembali ke indeks awal sebelum penamabahan, setelah itu di modulus lagi agar tetap sepanjang array.
#     return new_array
# print(circularArrayRotation([1, 2, 3],2 ,[0, 1, 2])) #2, 3, 1
# print(circularArrayRotation([1, 2, 3, 4],0 ,[0, 1, 2])) #2, 3, 1

#No. 36 Permutation Equation, https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
# buat rumus
# x = p[p[y]]
# for x in range(1, len(p)+1)

# p = [5, 2, 1, 3, 4]
# x=1==p[3], index 1 = 2, += 1 , = 3
# p[4] = 3, index 3 = 3, +=, = 4
# p[p[4]] = 1
# y = 4

# x=2==p[2], index 2 = 1, +=1, =2
# p[2]=2, index 2 = 1, +=1, =2
#p[p[2]] =2
# y =2
# def permutationEquation(p):
#     array = list(range(1, len(p)+1))
#     array_y = []
#     for num in array:
#         for item in p:
#             if num == item:
#                 index1 = p.index(item) + 1
#                 index2 = p.index(index1) + 1
#                 array_y.append(index2)
#     return array_y
# print(permutationEquation([2, 3, 1])) #2, 3, 1

#No. 37 Jumping on The Clouds, https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
# teradapat awan diberi nomor urut, biasa awan petir atau kumulus
# karakter melompat dari awan ke awan hingga mencapai awal lagi
# sederet awan (c)
# tingkat energi, e = 100
# karakter mulai dari c[0]
# 1 energi lompat se ukuran k, untuk mencapai awan c[(i+k)%n]
# jika mendarat di wan petir, c[i] = 1, energi e berkurang 3
# selesai ketika kembali ke cloud 0
# return nilai akhir e
# def jumpingOnClouds(c, k):
#     e = 100 # energi awal 100
#     i = 0 #indeks awal 0, ini posisi awal kita
#     while i < len(c): #kita while loop selama i kurang dari panjang c, nanti akan berhenti setelah memenuhi syarat break, yaitu indeksnya sama dengna 0 lagi
#         i = (i+k)% len(c) #ini rumus indeks melompat, agar melingkar, jadi melompat dulu dimana baru energinya berkurang
#         if c[i] != 1: #disini energi berkurang
#             e -= 1
#         else:
#             e -= 3    
#         if i == 0: #disini berhenti
#             break
#     return e
# print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2)) #92

# #no. 38 Find Digits, https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
# def findDigits(n):
#     divisors = []
#     digits = 0
#     str_n = str(n)
#     for num in str_n:
#         divisors.append(int(num))
#     for divisor in divisors:
#         if divisor != 0:
#             if n % divisor == 0:
#                 digits += 1
#     return digits
# print(findDigits(124)) #3
# print(findDigits(111)) #3
# print(findDigits(12)) #2
# print(findDigits(1012)) #3

# #No. 39 Append and Delete, https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
# # tambahkan huruf kecil di akhir string, dan hapus karakter terakhir dari string
# # buat list s menjadi t, jumlah langkahnya apa sama dengan k 
# # jika sama print "Yes" kalau tidak print "No"
# def appendAndDelete(s, t, k):
#     i = 0
#     line = min(len(s), len(t))
#     while i < line:
#         if s[i] != t[i]:
#             ops = len(s[i:]) + len(t[i:])
#             if ops == k:
#                 return "Yes"
#             elif k - ops > 0:
#                 if abs(ops-k)%2 == 0:
#                     return "Yes"
#                 elif i == 0 and abs(ops-k)%2 != 0:
#                     if len(s) == len(t):
#                         return "Yes"
#             elif k - ops < 0:
#                 return "No"
#         elif s[i:line] == t[i:line]:
#             diff = abs(len(s) - len(t))
#             if k - diff >= 0:
#                 if abs(diff-k)%2 == 0:
#                     return "Yes"
#                 elif abs(diff-k)%2 != 0:
#                     if len(s)+len(t)+1 == k:
#                         return "Yes"
#             elif k - diff < 0:
#                 return "No"    
#         i += 1
#     return "No"
    
# print(appendAndDelete("hackerhappy", "hackerrank", 9)) #Yes
# print(appendAndDelete("aba", "aba", 7)) #Yes
# print(appendAndDelete("aaaaaaaaaa", "aaaaa", 7)) #Yes
# print(appendAndDelete("ashley", "ash", 2)) #No
# print(appendAndDelete("zzzzz", "zzzzzzz", 4)) #Yes
# print(appendAndDelete("qwerasdf", "qwerbsdf", 6)) #No
# print(appendAndDelete("qwerty", "zxcvbn", 100)) #Yes
# print(appendAndDelete("aaa", "a", 5)) #Yes
# print(appendAndDelete("y", "yu", 2)) #No
# print(appendAndDelete("abcd", "abcdert", 10)) #No

# No. 40 Big Sorting, https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true
# urutkan elemen array dalam urutan bilangan bulat bertipe string
# return array yang diurutkan
##### Solusi 1, gagal karena terlalu lama
# def bigSorting(unsorted):
#     for i in range(len(unsorted)):
#         for j in range(len(unsorted)-1):
#             if len(unsorted[i]) < len(unsorted[j]):
#                 unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
#             elif len(unsorted[i]) == len(unsorted[j]) and unsorted[i] != unsorted[j]:
#                 k = 0
#                 while k < len(unsorted[i]):
#                     if int(unsorted[i][k]) < int(unsorted[j][k]):
#                         unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
#                         k = len(unsorted[i])
#                     k += 1
#     return unsorted
##### Solusi 2, gagal karena yang dibandingkan masih dalam bentuk integer
# def bigSorting(unsorted):
#     return sorted(unsorted, key=lambda x: (len(x), int(x)))
# Dalam ekspresi `key=lambda x: (len(x), int(x))`, kita menggunakan parameter `key` dari fungsi `sorted()` 
# untuk menentukan kunci pengurutan. Kunci pengurutan ini akan memberikan instruksi kepada Python tentang 
# bagaimana cara mengurutkan elemen-elemen dalam array.
# Sekarang, mari kita bahas bagian-bagian dari ekspresi tersebut:
# 1. `lambda x: ...`: Ini adalah fungsi lambda yang digunakan untuk membuat fungsi sederhana secara langsung
# tanpa harus mendefinisikan fungsi secara terpisah. Fungsi lambda ini akan menerima satu argumen `x`, yang 
# mewakili setiap elemen dalam array yang akan diurutkan.
# 2. `(len(x), int(x))`: Ini adalah bagian yang menentukan nilai kunci pengurutan untuk setiap elemen `x`. 
# Dalam hal ini, kita memiliki sepasang nilai `(len(x), int(x))` yang merupakan tuple. Tuple ini memiliki dua elemen:
#    - `len(x)`: Ini mengevaluasi panjang (jumlah karakter) dari elemen `x`. Dengan menggunakan `len(x)` sebagai 
# elemen pertama tuple, kita memberikan instruksi kepada Python untuk mengurutkan elemen berdasarkan panjangnya 
# dari yang terpendek ke yang terpanjang.  
#    - `int(x)`: Ini mengubah nilai `x` menjadi bilangan bulat. Dengan menggunakan `int(x)` sebagai elemen kedua 
# tuple, kita memberikan instruksi kepada Python untuk mengurutkan elemen secara numerik. Jika ada dua elemen dengan 
# panjang yang sama, mereka akan diurutkan berdasarkan nilai numeriknya dari yang terkecil ke yang terbesar.
# Dengan menggunakan `key=lambda x: (len(x), int(x))`, kita memberikan aturan pengurutan yang spesifik kepada fungsi
# `sorted()`. Hal ini memungkinkan Python untuk mengurutkan elemen-elemen array sesuai dengan kriteria yang telah
# ditentukan.
#### Solusi 3, berhasil
# def bigSorting(unsorted):
#     return sorted(unsorted, key=lambda x: (len(x), x))
# Pendekatan `key=lambda x: (len(x), x)` pada fungsi `sorted()` membandingkan string berdasarkan panjangnya terlebih 
# dahulu, dan jika panjangnya sama, maka string-string tersebut akan dibandingkan secara leksikografis, artinya 
# karakter-karakternya akan dibandingkan satu per satu.
# Mari kita bahas secara rinci:
# 1. `len(x)`: Bagian pertama dari kunci pengurutan mengevaluasi panjang (jumlah karakter) dari setiap string `x`. 
# Ini berarti string-string akan diurutkan terlebih dahulu berdasarkan panjangnya, sehingga string yang lebih pendek 
# akan muncul lebih awal dalam hasil pengurutan.
# 2. `x`: Bagian kedua dari kunci pengurutan adalah string itu sendiri. Jika panjang dua string sama, `x` akan 
# digunakan untuk membandingkan karakter-karakter dari kedua string tersebut. Karakter pertama dari setiap string 
# akan dibandingkan terlebih dahulu. Jika karakter-karakter pada posisi yang sama sama-sama sama, maka karakter 
# berikutnya akan dibandingkan, dan seterusnya. Ini akan terus berlanjut hingga ditemukan perbedaan di antara 
# karakter-karakter atau sampai kedua string habis. 
# Dengan menggunakan pendekatan ini, `sorted()` akan secara otomatis membandingkan karakter-karakter dari setiap 
# string pada posisi yang sesuai dalam urutan leksikografis. Oleh karena itu, string-string tersebut akan diurutkan 
# berdasarkan karakter-karakternya secara keseluruhan, bukan hanya berdasarkan karakter pertama.

# # No. 41 Sherlock and Squares, https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true
# # diberikan  nilai awal dan akhir dari rentang bilangan bulat, termasuk titik akhir
# # jumlah bilangan bulat persegi dalam rentang tersebut
# # bilangan bulat persegi adalah kuadrat dari bilangan tersebut
# def squares(a, b):
#     sums = int((b**0.5)//1) - int((a-1)**0.5//1)
#     return sums
# # import math

# # def squares(a, b):
# #     return int(math.sqrt(b)) - int(math.sqrt(a - 1))
# print(squares(3, 9))
# print(squares(17, 24))

# # # No. 42. Library Fine, https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true
# # # jika buku dikemalikan <= deadline, fine = 0
# # # jika buku dikembalikn > deadline, tapi masi dalam bulan dan tahun kelender yang sama, fine = 500 Hackos * (nomor hari telatnya)
# # # jiku buku dikembalika > bulan, tetapi masih dalam tahun kalender yang sama, fine = 500 Hackos * (nomor bulan telat)
# # # jika buku dikembalikan > tahun, fine = 1000 HAckos
# def libraryFine(d1, m1, y1, d2, m2, y2):
#     if y1 < y2:
#         fine = 0
#     elif y1 == y2: #kalau tahunnya sama
#         if m1 < m2:
#             fine = 0
#         elif m1 == m2: #kalau bulannya sama 
#             if d1 <= d2: #kalau ternyata harinya kurang sama dengan deadline
#                 fine = 0
#             if d1 > d2: #kalau harinya lebih dari deadline
#                 fine = 15 * (d1 - d2)
#         if m1 > m2: #kalau ternyata udah beda bulan
#             if m1 == (m2+1) and d1 < d2: #tapi belum sampai satu bulan kalau dihitung
#                 fine = 15 * (30 - d2 + d1)
#             else: # kalau emang udah lebih dari satu bulan
#                 fine = 500 * (m1 - m2)
#     elif y1 > y2: #kalau tahunnya udah beda
#         fine = 10000
#     return fine
# print(libraryFine(2, 7, 2015, 1, 2, 2014)) #10000
# print(libraryFine(1, 1, 2001, 1, 1, 2000)) #10000
# print(libraryFine(1, 1, 2015, 31, 12, 2014)) #10000

# #No. 43 Cut the Sticks, https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true
# # diberikan sejumlah tongkat dengan panjang berbeda-beda
# # kita akan memotong stick secara berulang-ulang menjadi stk yang lebih kecil
# # kemudian membuang potongn terpendek hingga tak bersisa
# # disetiap iteras akan didapatkan sisa batang terpendek, maka potong dan buang saat habis
# # jika semuanya sudah sama, maka semanya dipotong dengan janjang yang sama, maka tidak dibuang semuanya
# # cetak jumlah tongkat yang tersisa sebelum iterasi berikutnya
# def cutTheSticks(arr):
#     arr.sort()
#     sticks = [len(arr)]
#     length = len(arr)
#     stick = arr[0]
#     for i in arr:
#         if i == stick:
#             length -= 1
#         elif i != stick:
#             sticks.append(length)
#             stick = i
#             length -= 1
#     return sticks
# print(cutTheSticks([1, 13, 3, 8, 14, 9, 4, 4])) #8 7 6 4 3 2 1

# # No. 44 Repeated String, https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true 
# # ada tali s, dari huruf kecil bahasa inggris yang diulang berkali-kali tanpa batas.
# # diberikan bilangan bulat n
# # cari dan cetak jumlah huruf a yang pertamaa, n huruf dari string tak terbatas
# def repeatedString(s, n):
#     appear = 0
#     i = 0
#     while i < len(s):
#         if s[i] == "a":
#             appear += 1
#         i += 1
#     appears = appear * (n//len(s))
#     j = 0
#     while j < (n % len(s)):
#         if s[j] == "a":
#             appears += 1
#         j += 1
#     return appears
# print(repeatedString("a", 1000000000000))

# # No. 45 Jumping on Clouds, https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true
# # game dengan awan bernomor berurutan
# # sebagian awan petir sebagian awan kumulus
# # pemain bisa melompat ke awan kumulus manapun yang memiliki angka yang sama dengan angka plus awan saat ini (1 atau 2)
# # pemain harus menghindari petir
# # tentukan jumlah lompatan minimum yang diperlukan untuk melompat dari posisi awal ke akhir
# # 0 artinya kumuls, 1 artinya petir
# def jumpingOnClouds(c):
#     jump = 0
#     i = 0
#     while i < len(c)-1:
#         if i < len(c) - 2 and c[i+2] == 0:
#             jump += 1
#             i += 2
#         else:
#             jump += 1
#             i += 1
#     return jump
# print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))

# # No. 46. Equility in a Array, https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true
# # jumlah minimum elemn yang akan dihapus agar hanya yang sama yang tersisa
# def equalizeArray(arr):
#     length = 0
#     i = 0
#     while i < len(arr):
#         j = 0
#         appear = 0
#         while j < len(arr):
#             if arr[i] == arr[j]:
#                 appear += 1
#             j += 1
#         if appear > length:
#             length = appear
#         i += 1
#     return len(arr) - length
# print(equalizeArray([3, 3, 2, 1, 3]))

# #47. ACP-ICPC World, https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
# # tentukan jumlah maksimum topik yang dapat diketahui oleh tim yang terdiri dari dua orang
# # setiap subjek memiliki kolom dalam string biner
# # "1" berarti subjek diketahui sedangkan "0" berarti tidak
# # tentukan juga jumlah tim yang mengetahui jumlah topik maksimal
# # return array integer dua elemen, satu jumlah maksimal topik yang diketahui, yang kadua jumlah tim yang mengetahui topik tersebut
# def acmTeam(topic):
#     count_max = 0
#     same_team = 0
#     i = 0
#     while i < len(topic):
#         j = 0
#         while j < len(topic):
#             if i < j:
#                 k = 0
#                 count = 0
#                 while k < len(topic[i]):
#                     if topic[i][k] == "1" or topic[j][k] == "1":
#                         count += 1
#                     k += 1
#                 if count > count_max:
#                     count_max = count
#                     same_team = 1
#                 elif count == count_max:
#                     same_team += 1
#             j += 1
#         i += 1
#     return [count_max, same_team]
# print(acmTeam(["10101", "11100", "11010", "00101"]))

# #48. Taum  and Bday, https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=true
# # harus membeli b hadiah hitam dan w hadiah putih
# # harga hadiah hitam adalah bc unit
# # harga hadiah putih adalah wc unit
# # biaya untuk ubah kado hitam jadi kado putih adalah z unit
# def taumBday(b, w, bc, wc, z):
#     if bc + z < wc:
#         wc = bc + z
#     if wc + z < bc:
#         bc = wc + z
#     return b*bc + w*wc
# print(taumBday(3, 6, 9, 1, 1))

# #49. Keprekar Numbers, https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
# # bilangan keprekar adalah bilang integer yang jika dikuadratkan, kemudian dibagi dua karakternya, setelah itu dijumlahkan kembali, maka akan dapat nila yang sama dengan awal
# # bilangann bulat positif n dan d angka
# # persegi n, 2*d digit panjang atau (2*d)-1 panjang digit
# # pisahkan representasi string menjadi l dan r
# # bagian tangan kanan r harus d panjang digit
# # kiri adalah substring yang tersisa
# # ubah substring itu kembali menjadi bilangan bulat, lalu tambahkan
# # berhasil jika hasilnya n lagi
# # diberikan p dan q, p batas bawah, q batas atas
# # return daftar nomor keprekar yang dimodifikasi, dipisahkan spasi dalam satu baris, dan urutan menaik
# # jika tidak ada tulis 'INVALID RANGE'
# def kaprekarNumbers(p, q):
#     keprekar = []
#     for i in range(p, q+1):
#         sqr_str = str(i**2)
#         if len(sqr_str) == 1:
#             if i**2 == i:
#                 keprekar.append(i)
#         else:
#             d = len(sqr_str)//2
#             if_kp = int(sqr_str[:d]) + int(sqr_str[d:])
#             if if_kp == i:
#                 keprekar.append(i)
#     if not keprekar:
#         print("INVALID RANGE")
#     else:
#         for k in keprekar:
#             print(k, end=" ")
#     return
# kaprekarNumbers(1, 100)

# #No. 50, Flatland Space Stations, https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true
# # kota diberi nomor secara berurutan
# # masing-masing memiliki jalan 1km panjang yang menghubungkan ke kota berikutnya
# # bukan jalur melingkar, jadi kota pertama tidak terhubung dengan kota terakhir
# # tentukan jarak maksimum dari kota manapun hingga stasion luar angkasa terdekatnya
# def flatlandSpaceStations(n, c):
#     if len(c) == n:
#         return 0
#     c.sort()
#     range_max = max(c[0], n-c[-1]-1)
#     i = 0
#     while i < len(c)-1:
#         if (abs(c[i] - c[i+1]))//2 > range_max:
#             range_max = (abs(c[i] - c[i+1]))//2
#         i += 1
#     return range_max
# print(flatlandSpaceStations(20, [13, 1, 11, 10, 6]))

# #No. 51 Happy Lady Bugs, https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true
# # papan dilambangkan dengan string b
# # panjangnya n
# # i karakter string b[i], menunjukkan i sel papan
# # jika b[i] adalah _ artinya sel papan kosong
# # jika b[i] adalah alfabet kapital, artinya i berisi kepik berwarna b[i]
# # rangkaian b tidak akan mengandung karakter lain
# # kepik senang hanya jika sel kiri atau kanannnya berdekatan, b(i+1) ditempati oleh kepik lain yang memiliki warna yang sama
# # dalam satu gerakan bisa memindakan kepik ke sel kosong manapun
# # nilai-nilai n, dan b untuk g permainan kepik bahagia
# # apa mungkin membuat semua kepik bahagia, "YES" jika bisa, "NO" jika tidak
# def happyLadybugs(b):
#     if "_" not in b:
#         for i in range(1, len(b)-1):
#             j = 0
#             if b[i] != b[i+1] and b[i-1] != b[i]:
#                 return "NO"
#     i = 0
#     while i < len(b):
#         if b[i] != "_":
#             count = 0
#             j = 0
#             while j < len(b):
#                 if b[i] == b[j]:
#                     count += 1
#                 j += 1
#             if count == 1:
#                 return "NO"
#         i += 1
#     else:
#         return "YES"
# print(happyLadybugs("RRBBYY")) #YES
# print(happyLadybugs("X_Y__X")) #NO
# print(happyLadybugs("__")) #YES
# print(happyLadybugs("B_RRBR")) #YES

# No. 52. Strange Code, https://www.hackerrank.com/challenges/strange-code/problem?isFullScreen=true
# setiap detik angka yang ditampilkan dikurangi sebanyak 1 sampai mencpai 1
# detk berikutnya pengatur wktu disetel ulang ke 2*the_initial dan terus emnghitung mundur
# temukan dan cetk nilai yang ditampilkan oleh penghitung pada saat tu t.
# def strangeCounter(t):
    # time = 1
    # val = 3
    # valu = 3
    # while time < t:
    #     time += 1 
    #     if val == 1:
    #         valu *= 2
    #         val = valu 
    #     else :
    #         val -= 1  
    # return val
# def strangeCounter(t):
#     i = 3
#     while t > i:
#         t -= i
#         i *= 2
#     return i - t + 1
# print(strangeCounter(4))
# print(strangeCounter(1)) #3
# print(strangeCounter(7))

#No. 53 Super Reduced String, https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true
# kurangi string karakter huruf kecil
# dalam setiap operasi pilih sepasang huruf berdasarkan yang cocok dan hapus
# hapus karakter sebanyak mungkin menggunakan metode ini
# return string yang dihasilakn
# jika string terakhir kosong return "Empty String"
# def superReducedString(s):
#     empty = ""
#     for i in range(len(s)):
#         if len(empty) >= 1 and empty[-1] == s[i]:
#             empty = empty[:-1]
#         else:
#             empty += s[i]
#     if not empty:
#         return "Empty String"
#     else:
#         return empty
# print(superReducedString("aaabccddd")) #abd
# print(superReducedString("ggppppuurrjjooddwwyyllmmvvffddmmppxxaabbddddooppxxgghhhhvvnneeqqyyttbbffvvjjiiaammmmddddhhyywwqqiijj")) #Empty String

# #No. 54 Two Character, https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true
# # diberikn sebuah string
# # hapus karakter hingga string terdiri dari dua karkter bergantian
# # saat memilih karakter untuk dihapus maka semu akrakter harus dihapus
# # tentukan string terpanjang yang hanya terdiri dari dua karakter bergantian

# def alternate(s):
#     zig = "" #ini adalah wadah untuk string zigzag terpanjang
#     ss = "" #ini adalah wadah tempat karakter unik
#     for h in s: #pertama-tama kita forloop untuk dapatkan string krakter unik
#         if h not in ss:
#             ss += h
#     for i in range(len(ss)): #ini forloop untuk karakter satu
#         j = 0
#         while j < len(ss): #ini forloop untuk karakter dua
#             if i < j: #pakai ini agar karakternya tidak sama
#                 zag = "" #ini string sebagai wadah kandidat
#                 for k in range(len(s)): #kita forloop untuk membuat zigzag
#                     if s[k] == ss[i] or s[k] == ss[j]: #nah disini kalau karakter yang kita temukan sama dengan i dan j
#                         if len(zag) > 0 and zag[-1] == s[k]: #kita buat perintah dulu, kalau karakter yang kita temukan sama, udah aja udahan
#                             zag = ""
#                             break
#                         else: #lainnya kalau tidak sama, tambahkan ke kandidat
#                             zag += s[k]
#                 if len(zag) > len(zig): #nah disini, kalau zag lebih besar dari zig, maka zag jadi zig
#                     zig = zag
#             j += 1
#     print(zig)
#     return len(zig)
# print(alternate("pvmaigytciycvjdhovwiouxxylkxjjyzrcdrbmokyqvsradegswrezhtdyrsyhg")) #6
# print(alternate("muqqzbcjmyknwlmlcfqjujabwtekovkwsfjrwmswqfurtpahkdyqdttizqbkrsmfpxchbjrbvcunogcvragjxivasdykamtkinxpgasmwz")) #6
# print(alternate("uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon")) #6

# #No. 55 Insertion Sort 1, https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
# # diberikan dafar yang diurutkan dengan nomor yang tidak diurutkan e di sel paling kanan
# # apakah bisa menulis beberapa kode sederhana untuk dimasukkan e kedalam array agar tetap terurut
# def insertionSort1(n, arr):
#     e = arr[-1]
#     ar = arr
#     i = n-1
#     while ar[i] > e-1:
#         if i-1 != -1:
#             if e not in range(ar[i-1], ar[i]):
#                 ar[i] = ar[i-1]
#                 print(*ar)
#             elif e in range(ar[i-1], ar[i]):
#                 ar[i] = e
#                 return print(*ar)
#         elif i-1 == -1:
#             if e in range(ar[i]):
#                 ar[i] = e
#                 return print(*ar)
#         i -= 1
# insertionSort1(5, [2, 4, 6, 8, 3])
# insertionSort1(14, [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23])
# insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])

# #NO. 56 Strong Password, https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true
# # Password yang kuat adalah:
# # panjangnya minimal 6
# # berisi setidaknya satu digit
# # berisi setidaknya satu karakter huruf kecil
# # berisi setidaknya satu karakter huruf besar
# # setidaknya berisi satu karakter khusus
# def minimumNumber(n, password):
#     num = "0123456789"
#     low = "abcdefghijklmnopqrstuvwxyz"
#     upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     cha = "!@#$%^&*()-+"
#     num_c = 0
#     low_c = 0
#     upp_c = 0
#     cha_c = 0
#     len_c = len(password)
#     for i in password:
#         if i in num:
#             num_c = 1
#         if i in low:
#             low_c = 1
#         if i in upp:
#             upp_c = 1
#         if i in cha:
#             cha_c = 1
#     plus = 4 - sum([num_c, low_c, upp_c, cha_c])
#     if len_c + plus >= 6:
#         strong = plus
#     elif len_c + plus < 6:
#         strong = 6 - len_c
#     return strong
# print(minimumNumber(3, "Ab1"))
# print(minimumNumber(11, "#HackerRank"))
# print(minimumNumber(4, "4700"))

# #No. 57. Caesar Cipher, https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true
# # menggeser huruf dalam rotasi
# def caesarCipher(s, k):
#     low = "abcdefghijklmnopqrstuvwxyz"
#     upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     st = ""
#     idx = 0
#     while idx < len(s):
#         if s[idx] in low:
#             idj = low.find(s[idx])
#             idk = (idj + k) % 26
#             st += low[idk]
#         elif s[idx] in upp:
#             idj = upp.find(s[idx])
#             idk = (idj + k) % 26
#             st += upp[idk]
#         else:
#             st += s[idx]
#         idx += 1
#     return st

# #No 58. Missing Numbers, https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
# # temulan elemen dalam array kedua yang hilang di larik di pertama
# # return huruf yang hilang dalam urutan menaik, arr
# # jika ada beberapa nomor hilang yang sama kembalikan satu kali saja
# # perbedaan angka maksimum dan minimum <= 100
# def missingNumbers(arr, brr):
#     arr.sort()
#     brr.sort()
#     for g in arr:
#         brr.remove(g)
#     q_brr = set(brr)
#     brr = list(q_brr)
#     brr.sort()
#     return brr
# print(missingNumbers([203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
#                      [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]))

# # No. 59 Grid Challange, https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=false
# # atur ulang setiap baris berdasarkan abjad menaik
# # lihat apakah kolomnya juga dalam urutan abjad menaik? jika iya return "YES" else "NO"
# def gridChallenge(grid):
#     abj = "abcdefghijklmnopqrstuvwxyz"
#     grip = []
#     for i in range(len(grid)):
#         dig = []
#         for j in range(len(grid[i])):
#             idx = abj.find(grid[i][j])
#             dig.append(idx)
#         dig.sort()
#         grip.append(dig)
#     for l in range(len(grip[0])):
#         for k in range(len(grip)-1):
#             if grip[k][l] > grip[k+1][l]:
#                 return "NO"
#     return "YES"
# # print(gridChallenge(["kc", "iu"]))
# print(gridChallenge(["uxf", "vof", "hmp"])) #NO
# print(gridChallenge(["ppp", "ypp", "wyw"])) #YES
# print(gridChallenge(["lyivr", "jgfew", "uweor", "qxwyr", "uikjd"])) #NO
# print(gridChallenge(["l"])) #YES

# No. 60 Separate the Numbers
# string numerik dipecah menjadi dua atau lebi bilangan bulat positif, ketentuannya:
# selisih antara tiap elemnnya 1
# tidak ada angka nol di depan tiap elemnnya
# di cetak YES atau NO dan kemudian spasi angka awalnya
# def separateNumbers(s):
#     dig = 1
#     dig_f = 1
#     i = 0
#     while i < len(s)-dig-dig:
#         if s[0] != 0:
#             num1 = int(s[i:i+dig])
#             num2 = int(s[i+dig:i+dig+dig])
#             num3 = int(s[i+dig:i+1+dig+dig])
#             if num1 + 1 != num2 or num1 + 1 != num3:
#                 dig_f = dig
#                 dig += 1
#                 i -= 1
#             i += 1
#     if dig == len(s)/2:
#         return print("NO")
#     else:
#         return print(f'YES {s[0:0+dig_f]}')

# separateNumbers("91011")
# separateNumbers("010203")

# No. 61 Beautiful Triplets, https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true
# def beautifulTriplets(d, arr):
#     count = 0
#     arr.sort()
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if j > i :
#                 if arr[j] - arr[i] == d:
#                     for k in range(len(arr)):
#                         if k > j :
#                             if arr[k] - arr[j] == d:
#                                 count += 1
#     return count

# print(beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]))#3

# No. 62 Minimun Distances, https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true
# def minimumDistances(a):
#     range_min = len(a)+1
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if j > i :
#                 if a[i] == a[j]:
#                     range_ = j - i
#                     if range_ < range_min :
#                         range_min = range_
#     if range_min == len(a)+1:
#         range_min = -1
#     return range_min

# print(minimumDistances([7, 1, 3, 4, 1, 7])) #3


# No. 63 Halloween Sale, https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true
# def howManyGames(p, d, m, s):
#     total = 0
#     count = 0
#     price = p
#     if price < s:
#         total += price
#         count += 1
#         while price - d > m and total + price - d < s:
#             price -= d
#             total += price
#             count += 1
#         if count != 1 and total < s:
#             count += int((s - total) / m)
#     return count

# print(howManyGames(100, 19, 1, 180)) # 1
# print(howManyGames(100, 1, 1, 99)) # 0
# print(howManyGames(20, 8, 6, 85)) # 7

# No. 64 Chocolate Feast, https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=true
# def chocolateFeast(n, c, m):
#     feast = int(n/c) #disini kita pertama kali menghitung berap banyak coklat yang didapat
#     least = int(n%c) #disini kita hitung uang sisanya
#     count = feast #disini kita hitung total coklatnya
#     while int((feast + least)/m) > 0:
#         feast, least = int((feast + least)/m), int((feast + least)%m)
#         count += feast
#     return count

# print(chocolateFeast(16809, 123, 11668)) #136
# print(chocolateFeast(12, 4, 4)) #3
# print(chocolateFeast(6, 2, 2)) #5

def isPower(arr):
    # Write your code here
    result = []
    for num in arr:
        num_t = num
        while num_t >= 1:
            num_t = (num_t)*0.5
            if num_t != int(num_t):
                result.append(0)
                num_t = 0
            elif num_t == int(num_t):
                if num_t == 1 or num_t == 2:
                    result.append(1)
                    num_t = 0
                    
    return result
print(isPower([2, 3, 4])) #1, 0, 1