######################################
# MEDIUM #

# No. 1 Magic Square Forming, https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
# pertama-tama kita harus cek mana bilangan yang sama dari tiap baris, berarti kita harus tau posisinya dimana
# setelah itu bilangan yang sama itu kita bandingkan mana yang paling harus berubah agar baris dan kolom dan diagonal jadi pas 15
# def formingMagicSquare(s):
#     # Daftar semua kemungkinan persegi ajaib yang mungkin
#     magic_squares = [
#         [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
#         [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
#         [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
#         [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
#         [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
#         [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
#         [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
#         [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
#     ]

#     min_cost = float('inf')  # Inisialisasi biaya minimal
#     # Periksa setiap kemungkinan persegi ajaib
#     for magic_square in magic_squares:
#         cost = 0  # Reset biaya untuk setiap iterasi
#         # Periksa perbedaan untuk setiap angka pada setiap baris
#         for i in range(3):
#             for j in range(3):
#                 cost += abs(s[i][j] - magic_square[i][j])  # Hitung biaya perbedaan
#         min_cost = min(min_cost, cost)  # Perbarui biaya minimal jika perlu
#     return min_cost  # Kembalikan biaya minimal

# Uji coba fungsi
# print(formingMagicSquare([[2, 9, 8], [4, 2, 7], [5, 6, 7]]))  # Jawaban yang diharapkan: 21
# print(formingMagicSquare([[4, 4, 7], [3, 1, 5], [1, 7, 9]]))  # Jawaban yang diharapkan: 20
# print(formingMagicSquare([[4, 5, 8], [2, 4, 1], [1, 9, 7]]))  # Jawaban yang diharapkan: 14
# print(formingMagicSquare([[2, 2, 7], [8, 6, 4], [1, 2, 9]]))  # Jawaban yang diharapkan: 16

#2. Climbing The Leaderboard, https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
# pemain dengan skor tertinggi dapat skor nomor 1 di papan
# pemain dengan skor sama dapat peringkat sama, dan pemain berikutnya dapat peringkat berikutnya
# def climbingLeaderboard(ranked, player):
#     # Menghilangkan duplikat dan mengurutkan leaderboard
#     unique_ranked = sorted(set(ranked), reverse=True) #pertama-tama hilangkan duplikat dari skor di papan dengan set, setelah itu urutkan dengan fungsi sorted dan reverse
#     ranks_player = [] # ini list kosong untuk menyimpan peringkat pemain

#     j = len(unique_ranked) - 1 #
#     for score in player: #skor pemain diiterasi
#         while j >= 0 and score >= unique_ranked[j]: #kita nested loop dengan while, selama j tidak kurang dari 0 dan skor pemain lebih besar atau sama dengan skor peringkat itu, maka
#             j -= 1 # kita -j untuk loop ke rank selanjutnya
#         ranks_player.append(j + 2)  # jika sudah dapat maka tinggal ditambahkan ke list score pemain, ditambah 2 karena indeks sudah dikurang 1
#     return ranks_player

# # Contoh penggunaan
# print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))  # Output: [6, 4, 2, 1] 


# #No. 3 Extra Long factorials, https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
# def extraLongFactorials(n):
#     Fact = 1
#     for num in range(1, n+1):
#         Fact *= num
#     return print(Fact)
# print(extraLongFactorials(30))
# print(extraLongFactorials(25))
# print(extraLongFactorials(10))

# #No. 4 Non Divisible Subset, https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
# # diberikan sekumpulan bilangan bulat berbeda
# # cetak ukuran subset maksimal S
# # dimana isi subsetnya jika 2 elemennya dijumlahkan tidak habis dibagi rata k
# # return panjang maksimum subset array tersebut
# def nonDivisibleSubset(k, s):
#     # Inisialisasi kamus untuk menyimpan frekuensi sisa bagi
#     # dari pembagian setiap elemen dalam array dengan k.
#     # Kamus ini akan digunakan untuk menghitung berapa kali
#     # setiap sisa bagi muncul.
#     remainder_freq = {i: 0 for i in range(k)}
    
#     # Hitung frekuensi sisa bagi setiap elemen dalam array.
#     # Ini dilakukan dengan mengiterasi setiap elemen dalam array
#     # dan menghitung sisa bagi dari pembagian elemen tersebut dengan k.
#     for num in s:
#         remainder_freq[num % k] += 1
    
#     # Jumlahkan elemen dengan sisa bagi 0 atau k/2 (jika k genap).
#     # Elemen dengan sisa bagi 0 dapat berdiri sendiri dalam subset.
#     # Elemen dengan sisa bagi k/2 (jika k genap) juga dapat berdiri sendiri,
#     # karena jika dua elemen dengan sisa bagi k/2 digabungkan,
#     # hasilnya akan habis dibagi k.
#     max_length = min(remainder_freq[0], 1)
#     if k % 2 == 0:
#         max_length += min(remainder_freq[k // 2], 1)
    
#     # Jumlahkan elemen dengan sisa bagi (a, b) dan (b, a) di mana a + b = k.
#     # Misalnya, jika k = 5, maka elemen dengan sisa bagi (1, 4) dan (4, 1)
#     # harus digabungkan bersama, karena ketika dijumlahkan, hasilnya akan habis dibagi 5.
#     # Iterasi dilakukan hanya hingga setengah k untuk menghindari pengulangan.
#     for i in range(1, (k + 1) // 2):
#         max_length += max(remainder_freq[i], remainder_freq[k - i])
#     # jadi max length adalah penjumlahan dari bilangan dengan sisa bagi k, 0(satu atau kurang), genap(satu atau kurang), dan antara a atau b, dimana a+b = k
#     # Mengembalikan panjang maksimum subset yang memenuhi kondisi.
#     return max_length

# # Contoh penggunaan fungsi
# k = 4
# s = [19, 10, 12, 10, 24, 25, 22]
# print(nonDivisibleSubset(k, s))  # Output yang diharapkan: 3

# # No. 5 Organizing Containers of Balls, https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true
# # Setiap wadah hanya berisi bola-bola dengan jenis yang sama
# # tidak ada dua bola sejenis yang ditempatkan dalam wadah berbeda
# # jika berhasil print Possible dan jika tidak print Impossible
# # 111   0,0  0,1  0,2    300 
# # 111   1,0  1,1  1,2    030
# # 111   2,0  2,1  2,2    003
# def organizingContainers(container): #sebenarnya tujuan utamanya adalah untuk mengetahui apakah jumlah bola di container dan jenisnya itu sama atau tidak
#     # Pertama-tama kita buat list dari jumlah tiap container
#     num_balls = [sum(cont) for cont in container]
    
#     # Setelah menghitung jumlah bola dalam setiap kontainer, kita urutkan list num_balls tersebut.
#     # Sehingga akan mudah membandingkan jumlah bola dalam setiap kontainer dengan jumlah bola dari setiap jenis nanti.
#     num_balls.sort()
    
#     # Menghitung total bola dari setiap jenis dengan menjumlahkan setiap kolom dari matriks container.
#     # Kami membuat generator comprehension yang menjumlahkan elemen-elemen dalam setiap kolom dan kemudian mengurutkannya.
#     total_balls = sorted(sum(container[i][j] for i in range(len(container))) for j in range(len(container)))
    
#     # Memeriksa apakah jumlah bola dalam setiap kontainer sama dengan jumlah bola dari setiap jenis.
#     # Jika keduanya cocok, berarti kita dapat mengatur bola sesuai dengan aturan yang diberikan, 
#     # sehingga kondisi ini "Mungkin".
#     if num_balls == total_balls:
#         return "Possible"  # Jika kondisi di atas terpenuhi, kita mengembalikan string "Possible".
#     else:
#         return "Impossible"  # Jika kondisi di atas tidak terpenuhi, kita mengembalikan string "Impossible".

# # print(organizingContainers([[1, 1], 
# #                             [1, 1]])) #Possible
# # print(organizingContainers([[1, 2], 
# #                             [1, 1]])) #Impossible
# # print(organizingContainers([[999336263, 998799923], 
# #                             [998799923, 999763019]])) #Possible
# print(organizingContainers([[997612619, 934920795, 998879231, 999926463], 
#                             [960369681, 997828120, 999792735, 979622676], 
#                             [999013654, 998634077, 997988323, 958769423], 
#                             [997409523, 999301350, 940952923, 993020546]])) #Possible
# # Ketika jumlah bola dalam setiap kontainer sama dengan jumlah bola dari setiap jenis, 
# # itu berarti setiap jenis bola dapat diatur sedemikian rupa dalam kontainer-kontainer yang tersedia 
# # sehingga tidak ada konflik atau kesalahan dalam pengaturannya. 
# # Dengan kata lain, setiap jenis bola dapat ditempatkan dalam kontainer yang berbeda 
# # tanpa menyebabkan ketidakseimbangan jumlah bola pada setiap jenisnya.
# # Namun, jika jumlah bola dalam setiap kontainer tidak sama dengan jumlah bola dari setiap jenis, 
# # itu berarti tidak mungkin mengatur setiap jenis bola dalam kontainer-kontainer yang tersedia
# # tanpa menghasilkan konflik atau kesalahan dalam pengaturannya. 
# # Dalam kasus ini, ada jenis bola yang tidak dapat ditempatkan dengan benar dalam kontainer yang ada, 
# # sehingga penyusunan tidak mungkin dicapai dengan aturan yang diberikan.

# # No. 6 Encryption, https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# # spasi dihapus
# # dibuat dalam kotak len(s)**0.5
# # rows > columns?
# # rows * columns >= L
# # pilih grid dengan luas minimum, rows*columns
# # kemudian tampilkan sandi, per kolom jadi satu, dipisahkan spasi
# def encryption(s):
#     teks = s.replace(" ", "") #pertama-tama kita hilangkan spasi yang ada
#     sqr_len = len(teks)**0.5 #kita cari akar dari panjang teksnya
#     if len(teks)%sqr_len == 0 : #kalau akarnya dari dua bilangan sama maka kolom dan barisnya sama
#         column = row = int(sqr_len)
#     elif len(teks)%sqr_len != 0 : #kalau beda, kita cari
#         row = int(sqr_len)
#         column = int(sqr_len) + 1
#         if column*row < len(teks):
#             row +=1
#     grid = [] #ini kita buat per row
#     for i in range(row): #nah rangenya emang harus per row, karena pembagiannya sampai row ke-i
#         grid.append([])
#     index = 0
#     for i in range(row): #kita for loop untuk append ke grid tadi
#         j = 0
#         while j < column: #kita batasi sesuai panjang kolom
#             if index < len(teks):
#                 grid[i].append(teks[index])
#                 index += 1
#                 j += 1
#             else:
#                 j += 1
#     code = ""
#     for jdx in range(column): #kita for loop dengan patokannya pada kolom
#         for idx in range(row):
#             if jdx in range(len(grid[idx])):
#                 code += grid[idx][jdx]
#         code += " "
#     return code
# print(encryption("have a nice day"))
# print(encryption("feedthedog"))
# print(encryption("chillout")) #clu hlt io
# print(encryption("iuo")) #io u
# print(encryption("roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp")) #rlyzatp oxqkps quthvx fyegue qxrvdp ejinnr yfzgzf
# print(encryption("ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"))

# # # No. 7 Time in Words, https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true
# def timeInWords(h, m):
#     dict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 
#             11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fiveteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
#             20:"twenty", 30:"thirty", 40:"forty", 50:"fifty"}
#     if m == 00:
#         word = dict[h] + " o' clock"
#     elif m == 15:
#         word = "quarter past " + dict[h]
#     elif m == 30:
#         word = "half past " + dict[h]
#     elif m == 45:
#         word = "quarter to " + dict[h+1]
#     elif m != 00 and m < 30:
#         if m == 1:
#             word = dict[m] + " minute past " + dict[h]
#         elif m != 1 and m <= 19:
#             word = dict[m] + " minutes past " + dict[h]
#         else:
#             m1 = (m//10)*10
#             m2 = m%10
#             word = dict[m1] + " " + dict[m2] + " minutes past " + dict[h]
#     elif m != 00 and m > 30:
#         mr = 60 - m
#         if mr == 1:
#             word = dict[mr] + " minute past " + dict[h]
#         elif mr != 1 and mr <= 19:
#             word = dict[mr] + " minutes to " + dict[h+1]
#         else:
#             mr1 = (mr//10)*10
#             mr2 = mr%10
#             word = dict[mr1] + " " + dict[mr2] + " minutes to " + dict[h+1]
#     return word

# No. 8 3D Surface Area, https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true
# papan 2D A ukuran H*W
# H row, W column
# dibagi menjadi sel-sel ukuran 1*1
# setiap sel ditunjukkan dengan koordinat (i, j)
# sel(i, j) punya bilangan bulat A(i, j) tertulis di atasnya
# untuk membuat mainan tumpukan, A(i. j) jumlah ukuran kubus 1*1*1 di sel(i, j)
# papan menunjukkan nilai-nilai A(i, j)
# agar harga mainan sama dengan luas 3d tentukan harga mainan
# baris pertama adalah H dan W papan masing-masing
# selanjutnya setiap bilangan di sel sesuai koordinatnya
# def surfaceArea(A):
#     surface = 0
#     i = 0
#     while i < len(A):
#         j = 0
#         while j < len(A[i]):
#             surface += 2 #top and under
#             #front
#             if j in range(len(A[i])-1):
#                 if A[i][j] - A[i][j+1]  > 0:
#                     surface += A[i][j] - A[i][j+1] 
#             elif j not in range(len(A[i])-1):
#                 surface += A[i][j]
#             #rear
#             if j in range(1, len(A[i])):
#                 if A[i][j] - A[i][j-1] > 0:
#                     surface += A[i][j] - A[i][j-1]
#             elif j not in range(1, len(A[i])):
#                 surface += A[i][j]
#             #right
#             if i in range(len(A)-1):
#                 if A[i][j] - A[i+1][j] > 0:
#                     surface += A[i][j] - A[i+1][j]
#             elif i not in range(len(A)-1):
#                 surface += A[i][j]
#             #left
#             if i in range(1, len(A)):
#                 if A[i][j] - A[i-1][j] > 0:
#                     surface += A[i][j] - A[i-1][j]
#             elif i not in range(1, len(A)):
#                 surface += A[i][j]
#             j += 1
#         i += 1
#     return surface
# print(surfaceArea([[1]]))
# print(surfaceArea([[1, 3, 4],
#                   [2, 2, 3],
#                   [1, 2, 4]]))

# # 9 Greedy Florist, https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true
# # mengalikan harga setiap buaga dengan jumlah bunga yang diberi pelanggan sebelumnya ditambah 1
# # bunga pertama adalah harga asli,  (0+1)*original price, selanjutnya (1+1)*original price, dan seterusnya
# def getMinimumCost(k, c):
#     c.sort() #pertama kita urutkan bunga berdasarkan harga
#     c.reverse() #setelah itu balikkan, agar yang mahal di depan
#     price = 0 #disini kita jumlahkan harga
#     i = 0
#     while i < k: #kita bakal while loop setiap orang
#         j = 0 + i
#         plus = 1 #disini tempat penambahan perkalian harga
#         while j < len(c): #setelah itu kita while loop dengan bunga yang ada
#             price += c[j]*plus #kita tambahkan harga dengan buang itu
#             plus += 1
#             j += k #kita tambahkan k agar orang i ini akan langsung beli bunga berikutnya
#         i += 1
#     return price
# print(getMinimumCost(3, [1, 2, 3, 4])) #11

# 10 Flipping The Matrix, https://www.hackerrank.com/challenges/flipping-the-matrix/problem?isFullScreen=true
# permainan melibatkan a2n * 2n matriks
# setiap sel berisi bilangan bulat
# bisa membalikkan baris dan kolom manapun beberapa kali
# tujuannya untuk memaksimalkan jumlah elemen di dalamnya
# n*n matriks terletak di kuadran kiri atas matriks
# balik baris dan kolom setiap matriks sehingga jumlah elemen di kuadran kiri atas matriks maksimal
# jumlah maksimum yang mungkin dari quadran kiri atas n*n
# def flippingMatrix(matrix):
#     n = int(len(matrix)//2)
#     for jdx in range(0, len(matrix)):
#         max_j = 0
#         idx_mx = 0
#         for idx in range(0, len(matrix)):
#             if matrix[idx][jdx] > max_j:
#                 max_j = matrix[idx][jdx]
#                 idx_mx = idx
#         if idx_mx >= n:
#             for idx in range(0, n):
#                 var = matrix[-(idx+1)][jdx]
#                 matrix[-(idx+1)][jdx] = matrix[idx][jdx]
#                 matrix[idx][jdx] = var
#     sum = 0
#     for i in range(0, n):
#         max_i = 0
#         for j in range(0, n):
#             max_i += matrix[i][j]
#         max_i2 = 0
#         for j2 in range(n, len(matrix)):
#             max_i2 += matrix[i][j2]
#         if max_i2 > max_i:
#             sum += max_i2
#         elif max_i2 < max_i:
#             sum += max_i
#     return sum
# def flippingMatrix(matrix):
#     n = int(len(matrix)//2)
#     sums = 0
#     for i in range(0, n):
#         for j in range(0, n):
#             sums += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
#     return sums
# print(flippingMatrix([[112, 42, 83, 119],
#                      [56, 125, 56, 49],
#                      [15, 78, 101, 43],
#                      [62, 98, 114, 108]])) #414
# print(flippingMatrix([[107, 54, 128, 15],
#                       [12, 75, 110, 138],
#                       [100, 96, 34, 85],
#                       [75, 15, 28, 112]])) #488

#No. 11. Even Tree, https://www.hackerrank.com/challenges/even-tree/problem?isFullScreen=true
# diberi sebuah pohon
# temukan jumlah maksimum tepi yang dapat and hilangkan dari pohon untuk mendapatkan hutan
# sehinnga setiap komponen hutan yang terhubung berisi jumlah simpul genap
# def evenForest(t_nodes, t_edges, t_from, t_to):