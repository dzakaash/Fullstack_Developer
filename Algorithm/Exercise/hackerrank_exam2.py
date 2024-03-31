# #No. 1 Word Numbers!, selesai
# # https://edabit.com/challenge/HcLCh8566zewZvZ2j
# def word(s):
#     digits = {
#         "one": 1,
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eleven": 8,
#         "nine": 9,
#         "ten": 10
#     }
#     if s in digits:
#         return digits[s]
#     else:
#         return None
# word1 = word("one")
# word2 = word("two")
# word3 = word("nine")
# print(word1)
# print(word2)
# print(word3)

# #No. 2, Is the Word Singular or Plural? selesai
# # https://edabit.com/challenge/jozLzME3YptxydiQm
# def is_plural(word):
#     if word[-1] == "s":
#         return True
#     else:
#         return False
# word1 = is_plural("changes")
# word2 = is_plural("change")
# word3 = is_plural("dudes")
# word4 = is_plural("magic")
# print(word1)
# print(word2)
# print(word3)
# print(word4)

# #No. 3 Find the Odd Integer, belum
# # https://edabit.com/challenge/9TcXrWEGH3DaCgPBs
# def find_odd(lst): #buat fungsinya
#     while bool(len(lst)): #selama tidak 0 maka True, lanjut fungsi bawah
#         len_elemen = len(lst) #panjang elemen asumsikan sama dengan panjang list
#         i = frec = 0 #i bilangan yang dijadikan indeks asumsikan 0, frec sebagai banyaknya frekuensi kemunculan elemen asumsikan 0
#         bil =lst[0] #bil sebagai bilangan asumsikan bilangan pertama
#         while i < len_elemen: #selama indeks kurang dari panjang elemen, maka lanjutkan ke fungsi bawah
#             if lst[i] == bil : #jika elemen berdasarkan indeks sama dengan bil, maka
#                 frec += 1 #frekuensi ditambah satu
#                 lst.pop(i) #bilangan yang dibandingkan tadi dihilangkan
#                 len_elemen -= 1 #karena bilangannya hilang, maka panjangnya dikurangi satu
#             else : #jika bilagan itu tidak memenuhi syarat diatas, tidak ada yang sama
#                 i += 1 #maka, indeksnya ditambah satu, lanjut ke elemen selanjutnya
#         if frec % 2: #sekarang kita dapat nilai frekuensi, maka jika dibagi dua dan hasilnya nol, maka tidak lanjut, namun jika lebih dari nol dan hasilnya True
#             return bil #jika ada sisa, maka tampilkan bilangan tersebut
#         else:
#             return None #opsi jika sampai akhir tidak dapat frekuensi ganjil

# odd1 = find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
# odd2 = find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
# odd3 = find_odd([10])
# print(odd1)
# print(odd2)
# print(odd3)
                
# #No. 4 Tallest Birthday Cake Candles, done
# # # https://edabit.com/challenge/PtrPzWCWrPW54xfxK
# def birthday_cake_candles(candles): #buat fungsi
#     birthday = candles[0] #buat variabel baru (birthday) dan asumsi elemen pertama di list, kita anggap birthday adalah elemen terbesar
#     count = 0 #perhitungan asumsi awal 0
#     for i in candles: #buat for loop, dan variabel baru untuk menyebut elemen di list
#         if i > birthday: #buat syarat jika elemen di list lebih besar dari birthday
#             birthday = i #maka elemen itu jadi birthday
#             count = 1 #lalu perhitungan dari 0 jadi 1
#         elif i == birthday: #tapi kalau ternyata gk lebih besar namun serupa dengan birthday
#             count += 1 #perhitungannya jadi ditambah satu
#     return count #di return hasil count nya
# count1 = birthday_cake_candles([4, 4, 1, 3])
# count2 = birthday_cake_candles([3, 2, 1, 3])
# count3 = birthday_cake_candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25])
# print(count1)
# print(count2)
# print(count3)

# #No. 5 Check if All Values Are True, selesai
# # https://edabit.com/challenge/ogjDWJAT2kTXEzkD5
# def all_truthy(*args):
#     nilai = True
#     for angka in args:
#         if angka == False:
#             nilai = False
#             break
#     return nilai
# cek1 = all_truthy(True, True, True) 
# cek2 = all_truthy(True, False, True)
# cek3 = all_truthy(5, 4, 3, 2, 1, 0)
# print(cek1)
# print(cek2)
# print(cek3)

# #No. 6 The Forbidden Letter, selesai
# # https://edabit.com/challenge/pfuxt3J2p2tph3LJQ
# def forbidden_letter(char, lst):
#     letr = True
#     for huruf in lst:
#         if char in huruf:
#             letr = False
#             break
#     return letr
# cek1 = forbidden_letter("r", ["rock", "paper", "scissors"])
# cek2 = forbidden_letter("a", ["spoon", "fork", "knife"])
# cek3 = forbidden_letter("m", [])
# print(cek1)
# print(cek2)
# print(cek3)

# #No. 7 Free Coffee Cups, selesai
# # https://edabit.com/challenge/dcdy9QMBbryyWENcm
# def total_cups(n):
#     if n % 6 == 0:
#         jumlah = n + n / 6
#         return int(jumlah)
#     if n % 6 != 0:
#         jumlah = n + int(n/6)
#         return int(jumlah)
# total1 = total_cups(6)
# total2 = total_cups(12)
# total3 = total_cups(213)
# print(total1)
# print(total2)
# print(total3)

# #No. 8 Find the Missing Number, selesai
# # https://edabit.com/challenge/oMCNzA4DcgpsnXTRJ
# def missing_num(lst):
#     set1 = set(lst)
#     set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} #atau set(range(1, 11))
#     selisih = set2.difference(set1) #atau set2 - set 1
#     return list(selisih)[0]
# cek1 = missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])
# cek2 = missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])
# cek3 = missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9])
# print(cek1)
# print(cek2)
# print(cek3)
    
#No. 9 Sort Numbers in Ascending Order, belum
# https://edabit.com/challenge/gd9Yw3H4qGEt5xksN
def sort_nums_ascending(lst): #buat fungsinya dahulu
    for bubble in range(len(lst) -1, 0, -1): #buat variabel bubble untuk menyebut index dalam lst, di mana angkanya berurut terbalik
        for i in range(bubble): #panggil index itu dengan sebutan i jumlahnya diambil dari range bubble, gunanya agar
            if lst[i] > lst[i+1]: #jika suatu elemen lebih besar dari elemen selanjutnya
                var = lst[i] #maka var bernilai elemen itu
                lst[i] = lst[i+1]  #elemen itu menjadi bernilai dengan elemen selanjutnya
                lst[i+1] = var #maka elemen selanjutnya menjadi bernilai var, maka elemen itu akan bertukar tempat dengan elemen selanjutnya
        return lst #ditampilkan lst akhir
sort1 = sort_nums_ascending([1, 2, 10, 50, 5])
sort2 = sort_nums_ascending([80, 29, 4, -95, -24, 85])
sort3 = sort_nums_ascending([])
print(sort1)
print(sort2)
print(sort3)

# # #No. 10 Which Generation Are You? selesai
# # # https://edabit.com/challenge/68KgdtdwabrXydZFM
# def generation(x, y):
#     g = {
# 	-3: {
# 		"m": "great grandfather",
# 		"f": "great grandmother",
# 	},
# 	-2: {
#     	"m": "grandfather",
# 		"f": "grandmother",
# 	},
# 	-1: {
# 		"m": "father",
# 		"f": "mother",
# 	},
# 	0: {
# 		"m": "me!",
# 		"f": "me!",
# 	},
# 	1: {
# 		"m": "son",
# 		"f": "daughter",
# 	},
# 	2: {
# 		"m": "grandson",
# 		"f": "granddaughter",
# 	},
# 	3: {
# 		"m": "great grandson",
# 		"f": "great granddaughter",
# 	}
# }
#     if x not in g or y not in g[x]:
#         return None
#     calling = g[x][y]
#     return calling
# calling1 = generation(2, "f")
# calling2 = generation(-3, "m")
# calling3 = generation(1, "f")
# calling4 = generation(1, "b")
# print(calling1)
# print(calling2)
# print(calling3)
# print(calling4)
    
        
    