# #No.1 Stuttering Function, https://edabit.com/challenge/gt9LLufDCMHKMioh2
# def stutter(word):
#     phrase = (word[0]+word[1] + "... ")*2 + word + "?"
#     return phrase
# phrase1 = stutter("incredible")
# phrase2 = stutter("enthusiastic")
# phrase3 = stutter("outstanding")
# print(phrase1)
# print(phrase2)
# print(phrase3)

# #No.2 Find the Discount, https://edabit.com/challenge/cXnkmRdxqJrwdsP4n, belum
# def dis(price, discount):
#     disc = price - (discount/100) * price
#     print(disc)
#     disc_2coma1 = int(disc * 100 + 0.5)  # Menambah 0.5 sebelum pembulatan, sehingga jika angka sebelumnya lebih dari 4 akan dapat nilai satu
#     print(disc_2coma1)
#     disc_2coma = disc_2coma1 / 100
#     return disc_2coma

# print(dis(100, 75))  # harga 25
# print(dis(211, 50))  # harga 105.5
# print(dis(593, 61))  # harga 231.27
# print(dis(1693, 80)) # harga 338.6
# print(dis(700, 10))  # harga 630
# print(dis(1500, 50)) # harga 750
# print(dis(89, 20))   # harga 71.2

# #No.3 Radians to Degrees, https://edabit.com/challenge/2X2uZysLJ3CpsxLDD
# def radians_to_degrees(rad):
#     degrees = rad*180/3.14159 #jangan gunakan phi 22/7 karena 3.14159 lebih umum dan lebih mendekati phi sebenarnya
#     degrees_round = int(degrees * 10 + 0.5) / 10
#     return degrees_round
# print(radians_to_degrees(1)) #hasil 57.3
# print(radians_to_degrees(5)) #hasil 286.5
# print(radians_to_degrees(7)) #hasil 401.1
# print(radians_to_degrees(60)) #hasil 3437.7
# print(radians_to_degrees(100)) #hasil 5729.6
# print(radians_to_degrees(180)) #hasil 10313.2

# #No.4 Circle or Square, https://edabit.com/challenge/4me7LifXBwj5rhL4n
# def circle_or_square(rad, area):
#     per_circle = 2 * 3.14 * rad
#     per_square = 4 * (area)**0.5
#     if per_circle > per_square:
#         return True
#     else:
#         return False
# print(circle_or_square(16, 625))
# print(circle_or_square(5, 100))
# print(circle_or_square(8, 144))

# #No.5 Nomor Curzon, https://edabit.com/challenge/HYjQKDXFfeppcWmLX
# def is_curzon(num):
#     curz_up = 2**num + 1
#     curz_in = 2*num + 1
#     if curz_up % curz_in == 0:
#         return True
#     else:
#         return False
# print(is_curzon(5))
# print(is_curzon(10))
# print(is_curzon(14))

# #No.6 Luke, I Am Your ..., https://edabit.com/challenge/8pDH2SRutPoaQghgc
# def relation_to_luke(name):
#     relation = {
#         "Darth Vader" : "father",
#         "Leia" : "sister",
#         "Han" : "brother in law",
#         "R2D2" : "droid"
#     }
#     if not name:
#         return None
#     remind = "Luke, I am your " + relation[name] + "."
#     return remind
# print(relation_to_luke("Darth Vader"))
# print(relation_to_luke("Leia"))
# print(relation_to_luke("Han"))
# print(relation_to_luke("R2D2"))

# #No.7 Sum of Resistance in Series Circuits, https://edabit.com/challenge/gzmFeaXwFv8X6pBGq
# def series_resistance(lst):
#     if not lst:
#         return None
#     total = 0
#     for num in lst:
#         total = total + num
#     if total <= 1:
#         value = str(total) + " ohm"
#     else:
#         value = str(total) + " ohms"
#     return value
# print(series_resistance([1, 5, 6, 3])) #hasil 15 ohms
# print(series_resistance([0.2, 0.3, 0.4])) #hasil 0.9 ohm
# print(series_resistance([10,12, 1, 10])) #hasil 33 ohms
# print(series_resistance([10,13, 3.8, 20, 10])) #hasil 56.8 ohms
# print(series_resistance([0.5, 0.5])) #hasil 1.0 ohm
# print(series_resistance([16, 30, 22.8, 4])) #hasil 72.8 ohms
# print(series_resistance([20, 15, 32.5, 2])) #hasil 69.5 ohms
# print(series_resistance([52, 22, 20, 30])) #hasil 124 ohms
# print(series_resistance([10, 12, 32, 4.9, 5, 6, 71])) #hasil 140.9 ohms

# # No.8 Solving Exponential Equations With Logarithms, https://edabit.com/challenge/MhQbon8XzsG3wJHdP
# import math
# def solve_for_exp(a, b):
#     exp = math.log(b, a)
#     exp_round = int(int(exp * 10 + 0.5) / 10)
#     return exp_round
# print(solve_for_exp(4, 1024))
# print(solve_for_exp(2, 1024))
# print(solve_for_exp(9, 3486784401))

# #No.9 Invert Colors, https://edabit.com/challenge/i6hY9JSjQK4jcaB6i
# def color_invert(rgb):
#     inv_r = 255 - rgb[0]
#     inv_g = 255 - rgb[1]
#     inv_b = 255 - rgb[2]
#     return (inv_r, inv_g, inv_b)
# print(color_invert((255, 255, 255)))
# print(color_invert((165, 170, 221)))

# #No.10 End Corona!, https://edabit.com/challenge/uKPc5faEzQkMwLYPP
# def end_corona(recovers, new_cases, active_cases):
#     days = 0
#     while active_cases > 0:
#         active_cases = active_cases + new_cases - recovers
#         days += 1
#     return days
# print(end_corona(4000, 2000, 77000))
# print(end_corona(3000, 2000, 50699))
# print(end_corona(30000, 25000, 390205))

# #No.11 Basic Calculator, https://edabit.com/challenge/ZdnwC3PsXPQTdTiKf
# def calculator(num1, operator, num2):
#     if operator == "+":
#         hasil = num1 + num2
#     elif operator == "*":
#         hasil = num1 * num2
#     elif operator == "-":
#         hasil = num1 - num2
#     elif operator == "/":
#         if num2 == 0:
#             hasil = "Can't divide by 0!"
#         else:
#             hasil = num1 / num2
#     elif operator == "**":
#         hasil = num1**num2
#     else:
#         hasil = None
#     return hasil
# print(calculator(2, "+", 2))
# print(calculator(2, "*", 2))
# print(calculator(4, "/", 2))

# #No.12 Calculating Damage, https://edabit.com/challenge/HSHHkdRYXfgfZSqri
# def damage(damage, speed, time):
#     scale = {
#             "second" : 1,
#             "minute" : 60,
#             "hour" : 3600
#         }
#     if damage <= 0 or speed <= 0:
#         aps = "invalid"
#         return aps
#     else:
#         aps = damage * speed * scale[time]
#     return aps
# print(damage(40, 5, "second"))
# print(damage(100, 1, "minute"))
# print(damage(2, 100, "hour"))

################################
#No. 13 Let's Sort This List! https://edabit.com/challenge/NM8JbG5K2ajKjkqpj
def asc_des_none(lst, s):
    for bub in range(len(lst)):
        for i in range(0, len(lst) - bub -1):
            if s == "Asc":
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            elif s == "Des":
                if lst[i] < lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            elif s == "None":
                    lst == lst
    return lst
print(asc_des_none([4, 3, 2, 1], "Asc"))
print(asc_des_none([7, 8, 11, 66], "Des"))
print(asc_des_none([1, 2, 3, 4], "None"))

#No. 14 Return the Factorial, https://edabit.com/challenge/FF6kYPHdAcJnoosr5
# def factorial(num): #gunakan loop
#     fact = 1
#     for i in range(1, num+1):
#         fact *=i
#     return fact

# def factorial(num): #gunakan rekursi
#     if num == 0 or num ==1:
#         return 1
#     else:
#         return num * factorial(num-1)
# print(factorial(3))
# print(factorial(5))
# print(factorial(13))

# #No. 15 Number Split, https://edabit.com/challenge/9f3Mi6vHNcm8vRcSh
# def number_split(n):
#     split_lst = []
#     if n % 2 == 0:
#         split_lst.append(int(n / 2))
#         split_lst.append(int(n / 2))
#     elif n % 2 == 1:
#         if n >= 0:
#             split_lst.append(int(n / 2))
#             split_lst.append(int(n / 2) + 1)
#         elif n <= 0:
#             split_lst.append(int(n / 2) - 1)
#             split_lst.append(int(n / 2))
#     return split_lst
# print(number_split(4))
# print(number_split(10))
# print(number_split(11))
# print(number_split(-9))

# #No. 16 Same Parity? https://edabit.com/challenge/jzCGNwLpmrHQKmtyJ
# def parity_analysis(num):
#     str_num = str(num)
#     tot_dig = 0
#     for digits in str_num:
#         tot_dig = int(digits) + tot_dig
#     if num % 2 == tot_dig % 2:
#             return True
#     else:
#             return False
# print(parity_analysis(243))
# print(parity_analysis(12))
# print(parity_analysis(3))

#No. 17 Instant JAZZ: Alternation, https://edabit.com/challenge/jhghtvT2s58FnDr5T
# def jazzify(lst):
#     # if not lst:
#     #     return lst
#     i = 0
#     while i < len(lst): #jika False langsung lewat
#         if "7" in lst[i]:
#             lst[i] = lst[i]
#             i += 1
#         elif "7" not in lst[i]:
#             lst[i] = lst[i] + "7"
#             i += 1
#     return lst

# print(jazzify(["G", "F", "C"]))
# print(jazzify(["Dm", "G", "E", "A"]))
# print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
# print(jazzify([]))

# #No. 18 Hiding the Card Number, https://edabit.com/challenge/iRCwdDBkNcHM5QeAm
# def card_hide(card):
#     index = 0
#     card2 = ""
#     while index < len(card) - 4:
#         card2 += "*"
#         index +=1
#     card_final = card2 + card[-4:]
#     return card_final
# print(card_hide("1234123456785678"))

# #No. 19 Default Mood, https://edabit.com/challenge/tgEWKRQD8hu5dD3pX
# def mood_today(*mood):
#     if not mood:
#         feel = "Today, I am feeling neutral"
#     else:
#         feel = "Today, I am feeling " + mood[0]
#     return feel
# print(mood_today("happy"))
# print(mood_today("sad"))
# print(mood_today())

# #No. 20 Is it Time for Milk and Cookies? https://edabit.com/challenge/6nSckbgCx9hjTwmcw
# import datetime
# def time_for_milk_and_cookies(date):
#     if date.month == 12 and date.day == 24:
#         return True
#     else:
#         return False
# print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))
# print(time_for_milk_and_cookies(datetime.date(2013, 1, 23)))
# print(time_for_milk_and_cookies(datetime.date(3000, 12, 24)))
    