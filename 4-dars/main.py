'''  2. Amulohazaning qiymati rost bo‘lsin. “EMAS A YOKI A VA EMAS A” mulohoza
 natijasini chiqaruvchi dastur tuzing'''
# a = True
# print(not a or a and not a)

'''  3. A=false, B = true, C = true, D = false bo‘lsa, quyidagi ifodaning natijasini aniqlang.
 (((A && !B) || (C || D)) && !(A || B))'''
 
# a = False
# b = True
# c = True
# d = False
# print(((a and not b ) or (c or d )) and not (a or b) )

''' 4. Ikkita xaqiqiy son berilgan. Shu sonlardan kamida bittasi manfiy bo‘lsa, true qiymat
#  chiqaruvchi dastur tuzilsin.'''
 
# a = int(input(" a = "))
# b = int(input(" b = "))
# a_manfiy = a < 0
# b_manfiy = b < 0 
# print(a_manfiy + b_manfiy >= 1)

''' 5. Ikkita haqiqiy son berilgan. Shu sonlar har xil ishorali bo‘lsa, true qiymat chiqaruvchi
 dastur tuzing.'''
 
# a = int(input(" a = "))
# b = int(input(" b = "))
# print( (a > 0 and b < 0 )  or (a < 0 and b > 0) )

''' 6. Berilgan N sonining juft yoki toqligini tekshiruvchi dastur tuzing.'''

# n = int(input(" n = "))
# if n % 2 == 0 :
#     print(n, " juft son")
# else :
#     print(n ," toq son ")

''' 7. N soni juft bo‘lsa true natijasini ekranga chiqaring.'''

# n = int(input(" n = "))
# print(n % 2 == 0)

''' 8. Foydalanuvchi tomonidan kiritilgan natural sonning ikki xonali toq son ekanligini
aniqlovchi dastur tuzing.'''

# n = int(input(" n = "))
# print( 9 < n < 100 and n % 2 == 1)
# if 9 < n < 100 and n % 2 == 1 :
#     print(" ikki xonali toq son ")
# else :
#     print(" xatolik ")

''' 9. Foydalanuvchi tomonidan kiritilgan uch xonali natural sonning raqamlari turlicha
ekanligini aniqlovchi dastur tuzing.'''

# n = int(input(" n = "))
# n_1 = n % 10
# n_2 = (n // 10) % 10
# n_3 = n // 100
# if n_1 != n_2 and n_1 != n_3 and n_3 != n_2 and 99 < n < 1000 :
#     print(" bu son uch xonali va raqamlari bir xil emas")
# else:
#     print(" xatolik")

''' 10. Foydalanuvchi tomonidan kiritilgan uch xonali natural sonning "chapdan o'qiganda
ham, o'ngdan o'qiganda ham bir xil" ekanligini tekshiruvchi dastur tuzing. Agar bir xil
bo'lsa true aks holda false degan yozuv ekranga chiqarilsin'''

# n = int(input(" n = "))
# n_1 = n % 10 
# n_3 = n // 100
# print(99 < n < 1000 and n_1 == n_3)

''' 1. Uchta bir biriga teng bo‘lmagan a, b, c natural sonlar berilgan bo‘lsin.
Ularning ichidan eng kattasini topuvchi dastur tuzilsin.
Misol uchun: a = 12, b = 27, c = 19
Natija: 27'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# if a > b and a > c:
#     print(a , "eng katta son")
# elif b > a and b > c:
#     print(b, " eng katta son ") 
# else :
#     print(c , " eng katta son")    
    
''' 2. Uchta bir biriga teng bo‘lmagan A, B, C natural sonlar berilgan bo‘lsin.
Ushbu sonlarni o‘sish tartibida chiqaruvchi dastur tuzilsin.
Misol uchun: a = 19, b = 27, c = 12
Natija: 12, 19, 27'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))

# if a > b:
#     if b > c:
#         print(c, b, a)
#     else:
#         if c > a:
#             print(b, a, c)
#         else:
#             print(b, c, a)
# else :
#     if a > c:
#         print(a, c, b)
#     else:
#         if c > b:
#             print(a, b, c)
#         else:
#             print(a, c, b)

''' 3. Qiymati [-999; 999] oraliqda yotuvchi butun son berilgan. Son qiymatiga
mos ravishda “ikki xonali manfiy”, “nol soni”, “uch xonali musbat”
kabi satrlarni ekranga chiqaruvchi dastur tuzilsin.'''

# n = int(input(" n = "))

# if (n >= -99 and n <= -10) or (n >= 100 and n <= 999) or n == 0:
#     print(n)
# else:
#     print(" bu son shartlarga tushmaydi ")

''' 4. Qiymati [1; 9999] bo‘lgan x butun qiymatiga mos ravishda quyidagi
satrlarni chop soni berilgan. Bu sonning “to‘rt xonali juft son”, “ikki
xonali toq son” va … ekranga chiqaruvchi dastur tuzilsin.'''

# x = int(input(" x = "))
# if ((x >= 1000 and x <= 9999) and x % 2 == 0 ) or (x >= 10 and x <=99 and x % 2 == 1) :
#     print(x)
# else: 
#     print(" bu son shartlarga mos ")

''' 5. O‘quv yili davomida talaba to‘plagan reyting ballga mos ravishda uning
o‘zlashtirishi haqida xabar chiqaruvchi dastur tuzilsin.'''

# n = int(input(" n = "))

# if  0 < n <= 55:
#     print(" 2")
# elif 55 < n <= 70:
#     print(" 3")
# elif 70 < n <= 85:
#     print(" 4 ")
# elif 85 < n <= 100:
#     print(" 5 ")
# else:
#     print(" bunday baxo yo'q ")

''' 6. Jumlani rostlikka tekshiring: Berilgan uch xonali sonni chapdan
o‘qiganda ham, o‘ngdan o‘qiganda ham bir xil bo’lsa kiritilgan son
“palindirom” deb xabar chiqaruvchi dastur tuzilsin agar bir xil bo’lmasa
kiritilgan son “palindrom emas” degan yozuv ekranga chiqarilsin.
Misol uchun: a = 121
Natija: palindirom'''

# n = int(input(" n = "))
# n_1 = n % 10
# n_2 = n // 100
# if n_1 == n_2 and 99 < n <= 999:
#     print(n , " soni palindrom ")
# else:
#     print(n," soni palindrom emas ")    

''' 7. Jumlani rostlikka tekshiring: Berilgan uch xonali sonning raqamlari
ketma-ket o‘suvchi yoki kamayuvchi bo‘lib joylashgan deb yozuv
chiqaruvchi dastur tuzilsin.
Misol uchun:
a = 123, Natija: Ketma-ket o’suvchi;
a = 321, Natija: Ketma-ket kamayuvchi;'''

# n = int(input(" n = "))
# n_1 = n % 10
# n_2 = (n // 10) %10
# n_3 = n // 100
# if n_3 > n_2 and n_3 > n_1 and n_2 > n_1: 
#     print(" kamayuvchi raqamlar ")
# elif n_1 > n_2 and n_1 > n_3 and n_2 > n_3:
#     print(" o'suvchi raqamlar")    
# else:
#     print(" bu son o'suvchi ham kamayuvchi ham emas")  

''' 8. Jumlani rostlikka tekshiring: Berilgan uchta butun sonlarning hech
bo‘lmaganda ikkitasi bir biriga teng deb yozuv chiqaruvchi dastur
tuzilsin.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# if a == b or a == c or b == c:
#    print(" kamida ikktasi teng")
# else:
#     print(" xatolik")

''' 9. Aziz mashinada xarakatlanayotgan paytda bilmasdan qizil chiroqdan
o‘tib ketdi. Agar u jarimani 3 kun ichida to‘lasa 10% arzon to‘lov amalga
oshiradi. Agar u 15 kundan ortiq kun ichida jarimani o‘tkazib yuborsa
10% ortiq to'lov qiladi. (Foydalanuvchi tomonidan jarima miqdori va kun
kiritilsin)'''

# k = int(input(" kun kiriting = "))
# j = int(input(" jarimani kiriting = "))
# c = (j * 5 ) / 100

# if 0 < k <= 3:
#     print(j - c, " so'm to'lasin ")
# elif 3 < k <= 15:
#         print(j, " to'lasin")
# else:
#         print(j + c , " to'lasin ")
# if 16 <= k :
#     print( (k - 15) * c  + j)
    
    
''' 10. Issiqxona xarorati ichkaridagi o‘simliklar yaxshi rivojlanishi uchun
250 bo‘lishi lozim. Agar issiqxona xarorati 250 dan oshib ketsa “oynalar
ochilsin” aks holda 250 dan tushib ketsa “oynalar yopilsin” degan yozuv
chiqaruvchi dastur tuzilsin.
Misol uchun: n = 21
Natija: oynalar yopilsin'''

# x  = int(input(" xarorat kiritilsin = "))

# if x > 250:
#     print(" oynalar ochilsin")
# elif x ==  250:
#     print(" o'rtacha obi - havo")
# else:
#     print(" oynalarni yoping")

''' 11.Aqlli tesla mashinasi qizil chiroqni ko'rsa "harakatlanishdan to'xtang"
degan yozuv chiqadi, yoki sariq chiroq yonsa "harakatlanishga
tayyorlaning", aks holda, yashil chiroq yonsa "harakatlanishni davom
ettiring" degan yozuv chiqaruvchi dastur tuzilsin.
Masalan: Qizil
Natija: Harakatlanishdan to'xtang'''

# rang = str(input(" rangi kiriting : "))

# if rang == "qizil":
#     print(" harakatlanishdan to'xtang ")
# elif rang == "sariq":
#     print(" harakatlanishga tayyorlaning ")
# elif rang == "yashil":
#     print(" harakatlanishni davom ettiring ")
# else:
#     print(" bunday rang yo'q")

''' 12. Uchta son berilgan. Shu sonlarni avval kichigini keyin kattasini
ekranga chiqaruvchi dastur tuzilsin.
Misol uchun:
a = 12, b = 27, c = 19
Natija: min = 12, max = 27'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))

# if a >= b and a >= c:
#     print(" max = ", a)
# elif b >= a and b >= c:
#     print(" max = ", b)
# elif c >= a and c >= b:
#     print(" max = ", c)
# elif a >= b and c >= b:
#     print(" min = ", b)
# if a >= c and b >= c:
#     print(" min = ", c)
# elif c >= a and b >= a:
#     print(" min = ", a)
# else:
#     print(" boshqa son kiriting ")

''' 13. Ishchining oylik maoshi (salary) va o‘rnatilgan tartibdagi eng kam
oylik ish haqi (minimumWage) berilgan. Quyidagilar asosida ishchidan
olinadigan bir oylik daromad soliqni hisoblovchi dastur tuzilsin.
● Agar salary <= 5 * minimumWage bo‘lsa, 9%;
● Agar salary > 5 * minimumWage va salary <= 10 * minimumWage
bo‘lsa, 16%;
● Agar salary > 10 * minimumWage bo‘lsa, 23%.'''

# salary = int(input(" salary kiriting = "))
# miniumumage = 3
# s = (salary * 1 ) / 100
# if salary <= 5 * miniumumage:
#  print(" daramod solig'i ", s * 9)
# elif salary > 5 * miniumumage and salary <= 10 *miniumumage:
#     print(" daramod solig'i", s * 16) 
# elif salary > 10 * miniumumage:
#     print("  daramod solig'i ", s *23)       

''' 14. Foydalanuvchi tomonidan ushbu raqamlarga qo‘ng‘iroq amalga
oshirilsa vquyidagicha yozuv chiqaruvchi dastur tuzilsin.
● 101-o‘t o’chirish xizmati.
● 102-militsiya xizmati.
● 103-tez tibbiy yordam xizmati.
● 104-tabiiy gaz xizmati.'''

# t = int(input(" raqamni kiriting = "))
# if t == 101:
#     print(" o't o'chirish ")
# elif t == 102:
#     print(" militsiya xizmati ")
# elif t == 103:
#     print(" tez yordam xizmati ")
# elif t == 104:
#     print(" tabiiy gaz xizmati ")
# else: 
#     print(" mavjud bo'lmagan raqam terdingiz")

''' 15. Azizbek yangi sotib olgan kompyuteriga password “Aziz20” qo‘ydi.
Bir kuni ukasi Azizbekning ruxsatisiz kompyuteriga kirmoqchi bo‘ldi va
parolni terdi. Shu paytda agar password to‘g‘ri terilsa “Assalomu
alaykum Azizbek, Xush kelibsiz” aks xolda esa “Siz xato passwordni
kiritidingiz degan” yozuvni chiqaruvchi dastur tuzilsin. '''

# password = str(input(" parol kiriting = "))

# if password == "Aziz20":
#     print(" Assalomu alaykum Azizbek, Xush kelibsiz ")
# else:
#     print(" Siz xato passwordni kiritidingiz ")

''' 16. Sizda a, b va c harflari bilan lotereya chiptasi bor. Agar barcha
raqamlar bir-biridan farq qilsa, “Natija 0”. Agar barcha raqamlar bir xil
bo‘lsa, “Natija 20”. Agar ikkita raqam bir xil bo‘lsa, “Natija 10” kabi
yozuvlarni ekranga chiqaruvchi dastur tuzilsin'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))

# if a != b and b != c and a != c:
#     print(" natija 0 ")
# elif a == b == c :
#     print(" natija 20 ")
# elif a == b or a == c or b == c:
#     print(" natija 10")    

''' 17. Aqlli tesla mashinasida agar uning quvvat miqdori 20% dan kam
bo‘lsa “Mashinani qayta quvvatlang” degan yozuv, 21% dan 40%
gacha bo‘lsa “Mashinada kam zaryad miqdori mavjud”, 41% dan
100% gacha bo‘lsa “Mashinada quvvat miqdori yetarlicha” deb
yozuv chiqaruvchi dastur tuzilsin.'''

# q = int(input(" q  = "))

# if q < 20:
#     print(" qayta quvatlang ")
# elif 21 <= q < 40:
#     print(" mashinada kam zaryad mavjud ")
# elif 40 <= q <= 100:
#     print(" zaryad yetarli ")
# else:
#     print(" natog'ri raqam")        

''' 18. 1-99 oraliqdagi sonlar berilgan bo‘lsin. Foydalanuvchi tomonidan
kiritilgan sonni so‘zlar yordamida ekranga chiqaruvchi dastur tuzilsin.
Misol uchun: N = 12
Natija: o‘n ikki.'''

# n = int(input(" n = "))
# n_1 = n % 10
# n_2 = n // 10
# s = " "
# if n_2 == 1:
#    print


        
''' 19. Elektromobilning 100 km masofani bosib o‘tish uchun
akkumlatoridagi to‘liq quvvatning 40% sarflaydi. Ayni paytda uning
quvvati (energy) K% qolgan. Haydovchi D (distance) km masofaga
borishi uchun quvvat yetarli yoki yetarli emasligini aniqlang. Agar bor
quvvat yetarli bo‘lmasa, yana necha % quvvat kerakligi (required power)
ni aniqlang. Bunda K va D foydalanuvchi tomonidan kiritiladi.'''

# k = int(input(" k = "))
# d = int(input(" d = "))
# z = d - k * 2.5
# if   k * 2.5 >= d:
#     print(" yetarli ")
# elif k * 2.5 < d:
#     print(" yetarli emas ", z / 2.5, " foiz bo'lsa yetadi" )
    
    

