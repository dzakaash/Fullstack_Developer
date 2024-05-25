from flask import Flask, jsonify, request


app = Flask(__name__)

# 1. JSON Parameter
# Flipping The Matrix, https://www.hackerrank.com/challenges/flipping-the-matrix/problem?isFullScreen=true
# permainan melibatkan a2n * 2n matriks
# setiap sel berisi bilangan bulat
# bisa membalikkan baris dan kolom manapun beberapa kali
# tujuannya untuk memaksimalkan jumlah elemen di dalamnya
# n*n matriks terletak di kuadran kiri atas matriks
# balik baris dan kolom setiap matriks sehingga jumlah elemen di kuadran kiri atas matriks maksimal
# jumlah maksimum yang mungkin dari quadran kiri atas n*n
@app.route("/flipping", methods = ["PUT"])
def flippingMatrix():
    matrix = request.json.get("matrix")
    n = int(len(matrix)//2)
    sums = 0
    for i in range(0, n):
        for j in range(0, n):
            sums += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
    return jsonify({"sums": sums})
# print(flippingMatrix([[112, 42, 83, 119],
#                      [56, 125, 56, 49],
#                      [15, 78, 101, 43],
#                      [62, 98, 114, 108]])) #414
# print(flippingMatrix([[107, 54, 128, 15],
#                       [12, 75, 110, 138],
#                       [100, 96, 34, 85],
#                       [75, 15, 28, 112]])) #488

# 2. Form Parameter
# Strong Password, https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true
# # Password yang kuat adalah:
# # panjangnya minimal 6
# # berisi setidaknya satu digit
# # berisi setidaknya satu karakter huruf kecil
# # berisi setidaknya satu karakter huruf besar
# # setidaknya berisi satu karakter khusus
@app.route("/minimum", methods = ['POST'])
def minimum():
    password = request.form.get('password')
    num = "0123456789"
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cha = "!@#$%^&*()-+"
    num_c = 0
    low_c = 0
    upp_c = 0
    cha_c = 0
    len_c = len(password)
    for i in password:
        if i in num:
            num_c = 1
        if i in low:
            low_c = 1
        if i in upp:
            upp_c = 1
        if i in cha:
            cha_c = 1
    plus = 4 - sum([num_c, low_c, upp_c, cha_c])
    if len_c + plus >= 6:
        strong = plus
    elif len_c + plus < 6:
        strong = 6 - len_c
    return jsonify({'password': password,
                    'strong': strong})
# contoh masukan 'password' di form
# password : "Ab1", "#HackerRank", "4700"

# 3. Path Parameter
# Super Reduced String, https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true
# kurangi string karakter huruf kecil
# dalam setiap operasi pilih sepasang huruf berdasarkan yang cocok dan hapus
# hapus karakter sebanyak mungkin menggunakan metode ini
# return string yang dihasilakn
# jika string terakhir kosong return "Empty String"
@app.route('/Reduce/<s>')
def superReducedString(s):
    empty = ""
    for i in range(len(s)):
        if len(empty) >= 1 and empty[-1] == s[i]:
            empty = empty[:-1]
        else:
            empty += s[i]
    if not empty:
        return "Empty String"
    else:
        return jsonify({'empty': empty})
# print(superReducedString("aaabccddd")) #abd
# print(superReducedString("ggppppuurrjjooddwwyyllmmvvffddmmppxxaabbddddooppxxgghhhhvvnneeqqyyttbbffvvjjiiaammmmddddhhyywwqqiijj")) #Empty String

# 4. Header Parameter
# Append and Delete, https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
# # tambahkan huruf kecil di akhir string, dan hapus karakter terakhir dari string
# # buat list s menjadi t, jumlah langkahnya apa sama dengan k 
# # jika sama print "Yes" kalau tidak print "No"
@app.route('/append', methods = ['DELETE'])
def appendAndDelete():
    s = request.headers.get('s')
    t = request.headers.get('t')
    k = int(request.headers.get('k'))
    i = 0
    line = min(len(s), len(t))
    while i < line:
        if s[i] != t[i]:
            ops = len(s[i:]) + len(t[i:])
            if ops == k:
                return "Yes"
            elif k - ops > 0:
                if abs(ops-k)%2 == 0:
                    return "Yes"
                elif i == 0 and abs(ops-k)%2 != 0:
                    if len(s) == len(t):
                        return "Yes"
            elif k - ops < 0:
                return "No"
        elif s[i:line] == t[i:line]:
            diff = abs(len(s) - len(t))
            if k - diff >= 0:
                if abs(diff-k)%2 == 0:
                    return "Yes"
                elif abs(diff-k)%2 != 0:
                    if len(s)+len(t)+1 == k:
                        return "Yes"
            elif k - diff < 0:
                return "No"    
        i += 1
    return "No"
# print(appendAndDelete("hackerrank", "hackerhappy", 9)) #Yes
# print(appendAndDelete("aba", "aba", 7)) #Yes
# print(appendAndDelete("aaaaaaaaaa", "aaaaa", 7)) #Yes
# print(appendAndDelete("ashley", "ash", 2)) #No
# print(appendAndDelete("zzzzz", "zzzzzzz", 4)) #Yes
# print(appendAndDelete("qwerasdf", "qwerbsdf", 6)) #No
# print(appendAndDelete("qwerty", "zxcvbn", 100)) #Yes
# print(appendAndDelete("aaa", "a", 5)) #Yes
# print(appendAndDelete("y", "yu", 2)) #No
# print(appendAndDelete("abcd", "abcdert", 10)) #No

# 5. Query Parameter
# # Encryption, https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# # spasi dihapus
# # dibuat dalam kotak len(s)**0.5
# # rows > columns?
# # rows * columns >= L
# # pilih grid dengan luas minimum, rows*columns
# # kemudian tampilkan sandi, per kolom jadi satu, dipisahkan spasi
@app.route("/encryption", methods = ["GET"])
def encryption():
    s = request.args['s']
    teks = s.replace(" ", "") #pertama-tama kita hilangkan spasi yang ada
    sqr_len = len(teks)**0.5 #kita cari akar dari panjang teksnya
    if len(teks)%sqr_len == 0 : #kalau akarnya dari dua bilangan sama maka kolom dan barisnya sama
        column = row = int(sqr_len)
    elif len(teks)%sqr_len != 0 : #kalau beda, kita cari
        row = int(sqr_len)
        column = int(sqr_len) + 1
        if column*row < len(teks):
            row +=1
    grid = [] #ini kita buat per row
    for i in range(row): #nah rangenya emang harus per row, karena pembagiannya sampai row ke-i
        grid.append([])
    index = 0
    for i in range(row): #kita for loop untuk append ke grid tadi
        j = 0
        while j < column: #kita batasi sesuai panjang kolom
            if index < len(teks):
                grid[i].append(teks[index])
                index += 1
                j += 1
            else:
                j += 1
    code = ""
    for jdx in range(column): #kita for loop dengan patokannya pada kolom
        for idx in range(row):
            if jdx in range(len(grid[idx])):
                code += grid[idx][jdx]
        code += " "
    return code
# print(encryption("have a nice day"))
# print(encryption("feedthedog"))
# print(encryption("chillout")) #clu hlt io
# print(encryption("iuo")) #io u
# print(encryption("roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp")) #rlyzatp oxqkps quthvx fyegue qxrvdp ejinnr yfzgzf
# print(encryption("ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"))

app.debug = True
app.run(host="127.0.0.1", port=5000)