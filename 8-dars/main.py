''' 1. 1 dan 10 gacha bo‘lgan sonlarni ekranga chiqaruvchi dastur tuzing.'''

# for i in range(1,11):
#  print(i)

''' 2. Foydalanuvchi tomonidan kiritilgan songa mos karra jadvalini ekranga
chiqaruvchi dastur tuzing.'''
# son = int(input("Sonni kiriting : "))
# for i in range(1,11):
#     print(f"{son} * {i} = {son*i}")

''' 3. 1 dan 20 gacha bo'lgan juft sonlarni ekranga chiqaruvchi dastur
tuzing.'''

# for i in range(2,21,2):
#     print(i)

''' 4. 1 dan 20 gacha bo‘lgan toq sonlarni ekranga chiqaruvchi dastur
tuzing.'''

# for i in range(1 ,20 , 2):
#     print(i)

''' 5. a va b butun sonlari berilgan (a<b). Ular orasidagi butun sonlar
yig‘indisini chiqaruvchi dastur tuzing'''
# a = int(input("a = "))
# b = int(input("b = "))
# sum = 0
# for i in range(a+1, b):
#     sum +=i
# print(f"{a} va {b} sonlar oralig'idagi sonlar yeg'indisi {sum} ga teng")

''' 6. a va b butun sonlari berilgan (a<b). Ular orasidagi butun sonlar
ko‘paytmasini chiqaruvchi dastur tuzing.'''

# a = int(input("a = "))
# b = int(input("b = "))
# kopaytma = 1
# for k in range(a  + 1,b):
#     kopaytma *=k
# print(f"{a} va {b} sonlar oralig'idagi sonlar ko'paytmasi {kopaytma} ga teng")

''' 7. a va b butun sonlari berilgan (a<b). Ular orasidagi butun juft sonlarni
chiqaruvchi dastur tuzing.'''

# a = int(input("a = "))
# b = int(input("b = "))
# for son in range(a+1,b):
#    print(son)

''' 8. a va b butun sonlari berilgan (a<b). Ular orasidagi butun toq sonlarni
chiqaruvchi dastur tuzing'''

# a = int(input("a = "))
# b = int(input("b = "))
# for toq_son in range(a,b):
#     if toq_son % 2 == 1:
#         print(toq_son)

''' 9. a va b butun sonlari berilgan (a<b). Ular orasidagi butun juft sonlar
yig‘indisini va toq sonlarning ko‘paytmasini hisoblovchi dastur tuzing.'''

# a = int(input("a = "))
# b = int(input("b = "))

# sum = 0
# kopaytma = 1

# for son in range(a+1,b):
#     if son % 2 == 0:
#         sum += son
#     else:
#         kopaytma *=son
# print(f"{a} va {b} son oraligidagi juft sonlar yeg'indisi {sum} ga teng")
# print(f"{a} va {b} sonlar oraligidagi toq sonlar ko'paytmasi {kopaytma} ga teng)")
    
''' 10. N natural soni berilgan. Shu sonning natural bo‘luvchilarini
aniqlovchi dastur tuzing.'''

# n = int(input("n = "))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

''' 11. N natural soni berilgan. Shu sonning natural bo‘luvchilari
bo‘lmagan sonlarning yig‘indisini aniqlovchi dastur tuzing.'''

# n = int(input("n = "))
# sum = 0
# for i in range(1,n):
#     if n % i != 0:
#         sum +=i
# print(sum)

''' 12. N natural soni berilgan. Uning mukammal yoki mukammal son
emasligini aniqlovchi dastur tuzing.'''

# n = int(input("n = "))
# sum = 0
# for i in  range(1,n):
#     if n % i == 0:
#      sum +=i
#      if n == sum:
#            print(f"{n} soni mukammal son")
# if n != sum:
#     print(f"{n} soni mukammal son emas")

''' 13. N natural soni berilgan. Uning raqamlarining yig'indisini hisoblovchi
dastur tuzing.
Masalan: N = 1234; Natija: 1 + 2 + 3 + 4 = 10'''

# n = int(input("n = "))
# sum = 0
# for i in range(1,n):
#     boluvchi = n % 10
#     sum +=boluvchi
#     n //=10
# print(sum)

''' 14. a va b butun sonlar berilgan. Ulaning EKUBini topuvchi dastur
tuzing.'''
# a = int(input("a = "))
# b = int(input("b = "))


  


