# n = int(input(" n : "))
 
# match n:
#      case 1: print(" Dushanba")
#      case 2: print(" Seshanba")
#      case 3: print(" Chorshanba")
#      case 4: print(" Payshanba")
#      case 5: print(" Juma")
#      case 6: print(" Shanba")
#      case 7: print(" Yakshanba")
#      case _: print(' Bunday hafta kuni yo\'q')
''' 2. Foydalanuvchi tamonidan N natural soni kiritiladi. Kiritilgan songa mos oy
nomini ekranga chiqaruvchi dastur tuzilsin. Agar bunday Oy nomi mavjud
bo‘lmasa ekranga “Bunday oy nomi mavjud emas!” degan yozuv ekranga
chiqarilsin '''

# n = int(input(" n : "))
# match n:
#      case 1: print(" Yanvar")
#      case 2: print(" Fevral")
#      case 3: print(" Mart")
#      case 4: print(" Aprel")
#      case 5: print(" May")
#      case 6: print(" Iyun")
#      case 7: print(" Iyul")
#      case 8: print(" Avgust")
#      case 9: print(" Sentabr")
#      case 10: print(" Oktabr")
#      case 11: print(" Noyabr")
#      case 12: print(" Dekabr")
#      case _: print(' Bunday oy yo\'q')

''' 9. N butun soni berilgan. Baho natijalarini chiqaruvchi dastur tuzing. Agar N
soni 1-5 oraliqda bo'lmasa "xato" deb chiqaring.
1 - yomon
2 - qoniqarsiz
3 - qoniqarli
4 - yaxshi
5 - a'lo'''
# n = int(input(" n :"))
# match n:
#     case 1:print(" 1 - yomon")
#     case 2:print(" 2 - qoniqarsiz")
#     case 3:print(" 3 - qoniqarli")
#     case 4:print(" 4 - yaxshi")
#     case 5:print(" 5 - a'lo")
#     case _: print(" xato ")

''' 3. Foydalanuvchi tamonidan N natural soni kiritiladi. Kiritilgan songa mos fasl
nomini ekranga chiqaruvchi dastur tuzilsin. Agar bunday fasl nomi mavjud
bo‘lmasa ekranga “Bunday fasl nomi mavjud emas!” degan yozuv ekranga
chiqarilsin'''

# n = int(input(" n = "))

# match n:
#     case 1: print(" Qish fasli")
#     case 2: print(" Bahor fasli ") 
#     case 3: print(" Yoz fasli ")
#     case 4: print(" Kuz fasli ")
#     case _: print(" Bunday fasl nomi mavjud emas!")

''' 5. Foydalanuvchi tomonidan kiritilgan n sonini so'zlar yordamida ifodalovchi
dastur tuzilsin. n soni 1 dan katta va 100 dan kichik deb olinsin. Agar
kiritilgan n soni belgilangan orqaliqda mavjud bo'lmasa, siz kiritgan son
belgilangan chegarada aniqlanmadi degan yozuv ekranda aks ettirilsin.
Masalan: n = 123
Natija: bir yuz yigirma uch'''

# n = int(input(" n = "))
# n_1 = n % 10
# n_2 = n // 10

# match n_2:
#     case 1: print(" o'n ", end = "") 
#     case 2: print(" yigirma ", end = "") 
#     case 3: print(" o'ttiz ", end = "") 
#     case 4: print(" qirq ", end = "") 
#     case 5: print(" ellik ", end = "") 
#     case 6: print(" oltmish ", end = "") 
#     case 7: print(" yetmish ", end = "") 
#     case 8: print(" sakson ", end = "") 
#     case 9: print(" to'qson ", end = "") 
#     case 10: print(" yuz ", end = "")
#     case _: print(" bunday son yo'q", end = "")
# match n_1: 
#     case 0: print("")
#     case 1: print(" bir ")
#     case 2: print(" ikki ")
#     case 3: print(" uch ")
#     case 4: print(" to'rt")
#     case 5: print(" besh ")
#     case 6: print(" olti ")
#     case 7: print(" yetti ")
#     case 8: print(" sakkiz ")
#     case 9: print(" to'qqiz ")
#     case _: print(" bunday son yo'q")

''' 6. Foydalanuvchi tomonidan kiritilgan n sonini so'zlar yordamida ifodalovchi
dastur tuzilsin. n soni 1 dan katta va 1000 dan kichik deb olinsin. Agar
kiritilgan n soni belgilangan orqaliqda mavjud bo'lmasa, siz kiritgan son
belgilangan chegarada aniqlanmadi degan yozuv ekranda aks ettirilsin.'''

# n = int(input(" n = "))
# n_1 = n % 10
# n_2 = (n // 10) % 10
# n_3 = (n // 100) 
# n_4 = (n // 1000)
# match n_4:
#      case 1: print(" ming ", end = "") 
# match n_3:
#     case 0: print("")
#     case 1: print(" bir yuz", end="")
#     case 2: print(" ikki yuz", end="")
#     case 3: print(" uch yuz", end="")
#     case 4: print(" to'rt yuz", end="")
#     case 5: print(" besh yuz", end="")
#     case 6: print(" olti yuz", end="")
#     case 7: print(" yetti yuz", end="")
#     case 8: print(" sakkiz yuz", end="")
#     case 9: print(" to'qqiz yuz", end="")
#     case _: print(" bunday son yo'q", end="")
# match n_2:
#     case 0: print("")
#     case 1: print(" o'n ", end = "") 
#     case 2: print(" yigirma ", end = "") 
#     case 3: print(" o'ttiz ", end = "") 
#     case 4: print(" qirq ", end = "") 
#     case 5: print(" ellik ", end = "") 
#     case 6: print(" oltmish ", end = "") 
#     case 7: print(" yetmish ", end = "") 
#     case 8: print(" sakson ", end = "") 
#     case 9: print(" to'qson ", end = "") 
#     case 10: print(" yuz ", end = "")
#     case _: print(" bunday son yo'q", end = "")
# match n_1: 
#     case 0: print("")
#     case 1: print(" bir ")
#     case 2: print(" ikki ")
#     case 3: print(" uch ")
#     case 4: print(" to'rt")
#     case 5: print(" besh ")
#     case 6: print(" olti ")
#     case 7: print(" yetti ")
#     case 8: print(" sakkiz ")
#     case 9: print(" to'qqiz ")
#     case _: print(" bunday son yo'q")

''' 7. Foydalanuvchi tomonidan kiritilgan n sonini so'zlar yordamida ifodalovchi
dastur tuzilsin. n soni -100 dan katta -1 dan kichik deb olinsin. Agar
kiritilgan n soni belgilangan oraliqda mavjud bo'lmasa, siz kiritgan son
belgilangan chegarada aniqlanmadi degan yozuv ekranda chiqarilsin'''

# n = int(input(" n = "))
# if  n >= 0:
#     print(" Iltimos manfiy son kiriting:")
# else:
#   n_1 = (n- (n // 10) * 10)
#   n_2 = n // 10 
# match n_2:
#     case -1: print(" minus o'n ", end = "") 
#     case -2: print(" misus yigirma ", end = "") 
#     case -3: print(" minus o'ttiz ", end = "") 
#     case -4: print(" minus qirq ", end = "") 
#     case -5: print(" minus ellik ", end = "") 
#     case -6: print(" minus oltmish ", end = "") 
#     case -7: print(" minus yetmish ", end = "") 
#     case -8: print(" minus sakson ", end = "") 
#     case -9: print("minus to'qson ", end = "") 
#     case -10: print(" minus yuz ", end = "")
#     case _: print(" bunday son yo'q", end = "")
# match n_1: 
#     case -1: print(" minus bir ")
#     case -2: print(" minus ikki ")
#     case -3: print(" minus uch ")
#     case -4: print(" minus to'rt")
#     case -5: print(" minus besh ")
#     case -6: print(" minus olti ")
#     case -7: print(" minus yetti ")
#     case -8: print(" minus sakkiz ")
#     case -9: print(" minus to'qqiz ")
#     case _: print(" bunday son yo'q")

''' 9. N butun soni berilgan. Baho natijalarini chiqaruvchi dastur tuzing. Agar N
soni 1-5 oraliqda bo'lmasa "xato" deb chiqaring.
1 - yomon
2 - qoniqarsiz
3 - qoniqarli
4 - yaxshi
5 - a'lo'''

# m = int(input(" m = "))

# match m:
#     case 1: print(" yomon ")
#     case 2: print(" qoniqarsiz ")
#     case 3: print(" qoniqarli ")
    # case 4: print(" yaxshi ")
    # case 5: print(" a'lo ")
    # case _: print(" bunday baxo yo'q")
''' 10. Foydalanuvchi tomonidan oy raqami berilganda shu oyda necha kun
borligini aniqlovchi dastur tuzing.'''
# m = int(input(" m = "))

# match m:
#     case 1:print(" Bu yanvar oyi bunda 31 kun bor")
#     case 2:print(" Bu fevar oyi bunda 28 kun bor")
#     case 3:print(" Bu mart oyi bunda 31 kun bor")
#     case 4:print(" Bu aprel oyi bunda 30 kun bor")
#     case 5:print(" Bu may oyi bunda 31 kun bor")
#     case 6:print(" Bu iyun oyi bunda 30 kun bor")
#     case 7:print(" Bu iyul oyi bunda 31 kun bor")
#     case 8:print(" Bu avgust oyi bunda 31 kun bor")
#     case 9:print(" Bu yanvar oyi bunda 31 kun bor")
#     case 10:print(" Bu oktabr oyi bunda 30 kun bor")
#     case 11:print(" Bu noyabr oyi bunda 31 kun bor")
#     case 12:print(" Bu dekabr oyi bunda 31 kun bor")
#     case _:print(" Bunday oy yo'q")
        
    
    
    