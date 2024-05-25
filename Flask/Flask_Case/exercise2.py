from flask import Flask, request

app = Flask(__name__)


# No1. Separate the Numbers, https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true
# string numerik dipecah menjadi dua atau lebi bilangan bulat positif, ketentuannya:
# selisih antara tiap elemennya 1
# tidak ada angka nol di depan tiap elemnnya
# di cetak YES atau NO dan kemudian spasi angka awalnya
def separateNumbers(s):
    i = 1
    while i <= len(s) // 2: # Periksa dari 1 digit hingga setengah panjang string
        first_num = int(s[:i]) # Ambil potongan pertama dengan panjang i
        curr_num = first_num
        substr = str(first_num) # String untuk membangun pola
        while len(substr) < len(s): # Selama panjang substr kurang dari panjang s
            curr_num += 1
            substr += str(curr_num)
        if substr == s: # Jika pola yang dibangun sama dengan string s
            if str(first_num)[0] == '0': # Periksa apakah digit pertama nol
                return "NO"
            else:
                return "YES", first_num
        i += 1
    return "NO" # Jika tidak ditemukan pola yang sesuai

@app.route("/separate", methods = ["GET"])
def callSN():
    number = request.args.get("number")
    return separateNumbers(number)

# Contoh penggunaan
# print(separateNumbers("1234"))   # jawaban YES 1
# print(separateNumbers("91011"))  # jawaban YES 9
# print(separateNumbers("99100"))  # jawaban YES 99
# print(separateNumbers("101103")) # jawaban NO
# print(separateNumbers("010203")) # jawaban NO
# print(separateNumbers("13"))     # jawaban NO
# print(separateNumbers("4445"))   # jawaban YES 44
# print(separateNumbers("8889"))   # jawaban YES 88
# print(separateNumbers("8910"))   # jawaban YES 8

#No.2 Weighted Uniform String, https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=false
def weightedUniformStrings(s, q):
    uniform = set()
    weight  = ord(s[0])-96
    val = weight
    uniform.add(weight)
    for i in range(1, len(s)):
        val = ord(s[i])-96
        if s[i] != s[i-1]:
            weight = val
        elif s[i] == s[i-1]:
            weight += val
        uniform.add(weight)
    Strings = []
    for j in q:
        if j in uniform:
            Strings.append("Yes")
        else:
            Strings.append("No")
    return Strings
# print(weightedUniformStrings("abccddde", [1, 3, 12, 5, 9, 10]))

@app.route("/weight", methods = ["PUT"])
def callWUS():
    string = request.json["string"]
    queries = request.json["queries"]
    return weightedUniformStrings(string, queries)
    
# No. 3 Closest Numbers, https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=false
def closestNumbers(arr):
    arr.sort()
    diff = arr[1]-arr[0]
    result = []
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i] < diff:
            diff = arr[i+1]-arr[i]
            result = []
            result.append(arr[i])
            result.append(arr[i+1])
        elif arr[i+1]-arr[i] == diff:
            result.append(arr[i])
            result.append(arr[i+1])
    return result
# print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470 ]))

@app.route("/closest", methods = ["POST"])
def callCN():
    arr_num = request.json["Array Num"]
    return closestNumbers(arr_num)
            

if __name__ == '__main__':
    # Menjalankan aplikasi Flask
    app.run(debug=True)


