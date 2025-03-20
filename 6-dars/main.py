# a = "listen"
# print(a[2] + a[1] + a[0] + a[4] + a[5] + a[3])
''' 1. 2 ta string berilgan. Ularni qisqa+uzun+qisqa shaklida birlashishidan
 hosil bo'lgan matnni chiqaruvchi dastur tuzing.
 Masalan: s1 = "salom" s2 = "alik" natija: aliksalomalik'''
# a = str(input(" A:"))
# b = str(input(" B:"))

# if len(a) > len(b):
#       print(b + a + b) 
# else:
#     print(a + b + a)

''' 2. N1, N2 natural sonlari va s1, s2 satrlari berilgan. S1 satrning
 boshlang'ich N1 ta belgisidan va s2 satrning oxirgi N2 ta belgisidan
 iborat yangi satr hosil qiluvchi dastur tuzing.'''

# s_1 = str(input(" s_1:"))
# n_1 = int(input(" n_1:"))
# s_2 = str(input(" s_1:"))
# n_2 = int(input(" n_2:"))
# print(s_1[:n_1] + s_2[-n_2:])

''' 3. Name nomli satr berilgan, masalan "Ozoda", ekranga ushbu
ko'rinishdagi matnni chiqaring:
"Salom, Ozoda"'''

# Name = input("Name = ")
# print(f"Salom,{ Name}")

''' 4. 2 ta a va b satr berilgan. a satr uzunligi 4 ga tengligi ma’lum. a satrni
2 va 3-harflari o’rtasiga b satrni joylashtirib natijani qaytaruvchi dastur
tuzing.
Masalan: a = "<<>>", b = "Salom", natija: "<<Salom>>"'''

# a = input(" a = ")
# b = input(" b = ")
# if len(a) > 5:
#   print(a[0] + a[1] + b + a[2] + a[3])
# else:
#     print(" a string uzunligi 4 dan uzun")

''' 5. Uzunligi kamida 2 ga teng bo'lgan satr berilgan. Shu satrni oxirgi 2 ta
harfini 3 marta yonma-yon qilib ekranga chiqaruvchi dastur tuzing
Masalan: a = "Hello" natija: "lololo"'''

# a = input(" a = ")
# if len(a) >= 2:
#     print((a[-2] + a[-1]) * 3) 
# else:
#     print(" a string uzunligi 2 dan kichik ")

''' 6. Satr berilgan. Ushbu satrni birinchi 2 ta harfini ekranga chiqaring. Agar
satr uzunligi 2 dan kichik bo'lsa, o'sha satrni o'zini chiqaruvchi dastur
tuzing.
Masalan: a = "Hello" natija: "He" a = "2" natija: "2"'''

# a = input("a = ")
# if len(a) >= 2:
#     print(a[0] + a[1])
# else:
#     print(a)

''' 7. Juft uzunlikdagi satr berilgan. Shu satrni birinchi yarmini qaytaruvchi
dastur tuzing.'''

# a = input("a = ")
# if len(a) % 2 == 0:
#     print(a[:len(a)//2])
# else:
#     print(" a juft emas")
    
''' 8. Kamida 2 ta harfdan iborat satr berilgan. Shu satrni boshidagi va
oxiridagi harflarisiz chiqaruvchi dastur tuzing.
Masalan: a = "Hello" natija: "ell"'''

# n = input("n = ")
# if len(n) >= 2:
#   x = n[1:-1]
#   print(x)
# else:
#     print(" xatolik ")

''' 9. Uzunligi kamida 1 ga teng bo’lgan 2 ta satr berilgan. Ushbu satrlarni
1-harflarini hisobga olmasdan hisobga olmasdan, satrlarni qo'shib
chiqaruvchi dastur tuzing.
Masalan: a = "Hello" b = "There" natija: "ellohere"'''
# n = input("n = ")
# m = input("m = ")
# if len(n) >= 1 and len(m) >= 1:
#     print(n[1:] + m[1:])
# else:
#     print(" xatolik")

''' 10. Satr berilgan. Satrni birinchi 2 ta harfini olib, davomiga qo’yib
chiqaruvchi dastur tuzing.
Masalan: a = "Hello" natija: "lloHe"'''

# n = input("n = ")
# print(n[1:] + n[0] + n[1])

''' 11. s string va b bool berilgan. Agar b o'zgaruvchi True bo'lsa, s'ning
birinchi harfini, aks holda s'ning oxirgi harfini ekranga chiqaruvchi
dastur tuzing'''

# s = "hello"
# b = input(" b = ")
# if b == "True":
#     print(s[0])
# elif b == "False":
#     print(s[-1])
  
'''
capitalize() ->  bu method bizga gapimizdagi birinchi so'zni upper qilib beradi
casefold() -> bu method bizga gapimizdagi so'zlarni lower harifga alishtirib beradi bu lower() methodga similar
center() -> bu method bizga stringimizni center() ichiga qiymat bersak shu qiymat orasida joylashtirib beradi
biz center() methodda buyruq berishimiz mumkin misol uchun center(20, 0) -> bunda stringiimizni 20 orasiga ikkki yoniga esa 
o qo'yib chiqadi

'''