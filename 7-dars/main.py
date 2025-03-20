''' 1. 1 dan 10 gacha bo‘lgan sonlarni ekranga chiqaruvchi dastur tuzing'''
# i = 1
# while i <= 10:
#     print( i )
#     i +=1

''' 2. Foydalanuvchi tomonidan kiritilgan songa mos karra jadvalini ekranga
chiqaruvchi dastur tuzing.'''
# son = int(input("son kiriting "))
# i = 1
# while i <= 10:
#     print(f" {son} * {i} = {son * i }")
#     i +=1

''' 3. 1 dan 20 gacha bo'lgan juft sonlarni ekranga chiqaruvchi dastur
tuzing.'''

# i = 1
# while i <= 20:
#    i += 1
#    if i % 2 ==0:
#        print(i)

''' 4. 1 dan 20 gacha bo‘lgan toq sonlarni ekranga chiqaruvchi dastur
tuzing.'''

# i = 0
# while i <= 20:
#     i +=1
#     if i % 2 == 1:
#         print(f"Toq sonlar: {i}")

''' 5. a va b butun sonlari berilgan (a<b). Ular orasidagi butun sonlar
yig‘indisini chiqaruvchi dastur tuzing '''

# son1 = int(input(" son1 kiriting = "))
# son2 = int(input(" son2 kiriting = "))
# sum = 0
# while son1 < son2 - 1:
#     son1 +=1
#     sum = sum +son1
    
# print(f"Yeg'indi:{sum}")

'''6. a va b butun sonlari berilgan (a<b). Ular orasidagi butun sonlar
ko‘paytmasini chiqaruvchi dastur tuzing'''

# son1 = int(input(" son1 = "))
# son2 = int(input(" son2 = "))

# kopaytma = 1
# while son1 < son2 -1:
#     son1 +=1
#     kopaytma = kopaytma * son1
    
# print(f"kopaytma: {kopaytma}")

''' 7. a va b butun sonlari berilgan (a<b). Ular orasidagi butun juft sonlarni
chiqaruvchi dastur tuzing.'''

# son1 = int(input(" son1 = "))
# son2 = int(input(" son2 = "))

# while son1 < son2 -1:
#     son1 +=1
#     if son1 % 2 == 0:
#         print(son1)

''' 8. a va b butun sonlari berilgan (a<b). Ular orasidagi butun toq sonlarni
chiqaruvchi dastur tuzing.'''

# son1 = int(input(" son1 = "))
# son2 = int(input(" son2 = "))

# while son1 < son2 - 1:
#     son1 +=1
#     if son1 % 2 ==1:
#         print(son1)

''' 9. a va b butun sonlari berilgan (a<b). Ular orasidagi butun juft sonlar
yig‘indisini va toq sonlarning ko‘paytmasini hisoblovchi dastur tuzing'''

# son1 = int(input(" son1 = "))
# son2 = int(input(" son2 = "))
# sum = 0
# kopaytma = 1

# while son1 < son2 -1:
#     son1 +=1
#     if son1 % 2 == 0:
#         sum = sum + son1
#     else:
#         kopaytma = kopaytma * son1
# print(f" juft sonlar sonni yeg'indisi {sum}")
# print(f"toq sonlar qiymati ko'paytmasi {kopaytma}")

''' 10. N natural soni berilgan. Shu sonning natural bo‘luvchilarini
aniqlovchi dastur tuzing.'''

# son = int(input("son = "))
# boluvchi = 1
# while boluvchi < son  :
#     boluvchi += 1
#     if son % boluvchi == 0:
#         print(boluvchi)

''' 11. N natural soni berilgan. Shu sonning natural bo'luvchilari
bo'lmagan sonlarning yig'indisini aniqlovchi dastur tuzing'''

# son = int(input("son = "))
# boluvchi = 1 
# sum = 0
# while boluvchi <= son:
#       if son % boluvchi != 0:
#          sum +=boluvchi
#       boluvchi+=1
# print(sum)

''' 12. N natural soni berilgan. Uning mukammal yoki mukammal son
emasligini aniqlovchi dastur tuzing. Mukammal sonlar oʻzidan farqli bo‘luvchilarning yig‘indisiga teng
natural sonlar.
Masalan: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14'''

# son = int(input("son = "))
# sum = 0
# boluvchi = 0
# while boluvchi < son -1 :
#       boluvchi += 1
#       if son % boluvchi == 0:
#         sum = sum + boluvchi
# if son == sum:      
#          print(f" {son} mukammal son hisoblanadi")
# else:
#     print(" Mukammal son emas")

''' 13. N natural soni berilgan. Uning raqamlarining yig'indisini hisoblovchi
dastur tuzing.
Masalan: N = 1234; Natija: 1 + 2 + 3 + 4 = 10'''

# son = int(input("son = "))
# sum = 0
# while son != 0:
#     qoldiq = son % 10
#     sum = sum + qoldiq
#     son //= 10
# print(sum)

# while 1

# A = int(input("A = "))
# B = int(input("B = "))
# while A > B:
#     A -= B
# print(f" Qolgan ortiqcha joyi {A} ")

# while 2

# A = int(input("A = "))
# B = int(input("B = "))
# sanagich = 0
# while A > B:
#     A -=B
#     sanagich +=1
# print(sanagich) 

# while 3

# son1 = int(input("son1 = "))
# son2 = int(input("son2 = "))
# while son1 > son2:
#     son1 -=son2
# print(f" son1 ni son2 ga bo'lgandagi qoldig'imiz {son1} ga teng")

# while 4 ishlay olmadim

# son = int(input("son = "))
# while son > 0 :
#     son 
# if son == 1:
#         print(f" bu son  uchning darajasi")
# else:
#      print(f" bu son uchning darajasi emas") 

# while 5

# n = int(input("n = "))
# k = 0
# saqlagich = n
# while n  % 2 == 0:
#     n //=2
#     k +=1
# if n == 1:
#         print(f"{saqlagich} soni ikkining {k} darajasi")
# else:
#         print(f"{saqlagich}  2 ning darajasi emas") 

# while 6


