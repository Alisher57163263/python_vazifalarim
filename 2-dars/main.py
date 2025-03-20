# L = 250 
# m = L / 100
# print(m)
# L = int(input(' L ni kiritig = '))
# m = L/100
# print(m)

# M = int(input(" og'irlkni kiriting = " ))
# T = M / 1000
# print(T)

# a = int(input(' fayl hajmini baytda kiriting = '))
# b = a/1024
# print(a,"bayt", b,"kbga teng")

# n = int(input(' n sonini kiriting = '))
# n_10 = n // 10
# n_1 = n % 10
# print(n_10, "o'nlar xonasi ", n_1, "birlar xonasi")

# 5
# n = int(input(' sonni kiriting = '))
# n_10 = n // 10
# n_1 = n % 10
# print(n_10 + n_1 , 'raqamlar yegindisi')

# 6
# n = int(input('raqamni kiriting = '))
# n_10 = n//10
# n_1 = n % 10
# print(n_1 * 10 + n_10)

# 7
# n = int(input('99 dan katta son kiriting = '))
# n_100 = n //100
# print(n_100) 

# 8
# n = int(input(' yuzlar xonasidagi raqam kiritin = '))
# n_10 = n % 10

# n_1 = (n//10)%10
# print("son",n_10)
# print(n_1)

# uyga vazifalar
'''1. Uzunlik L santimetrda berilgan. Undagi metrlar sonini aniqlang.
 (1 metr = 100 santimetr '''
 
# L = int(input(" uznulikni sm kiriting = "))
# M = L / 100
# print(L , " sm ", M, " metga teng ") 

'''2. Og'irlik M kilogrammda berilgan. Undagi to'liq tonnalar sonini
 aniqlovchi dastur tuzilsin.
 (1 tonna = 1000 kg)'''
 
# M = int(input(" og'irlikni kgda kiriting = "))
# T = M / 1000
# print(M, " kg ", T, " tonnaga teng ")

'''  3. Faylning hajmi baytlarda berilgan. Fayl hajmini to'liq kilobaytlarda
 ifodalovchi dastur tuzing.
 (1024 bayt = 1kb'''
 
# B = int(input(" malumot baytini kiriting = "))
# K = B / 1024
# print(B , " bayt", K," kbga teng") 

''' 4 Ikki xonali son berilgan. Oldin uning o'nliklar xonasidagi raqamni,
 so'ng, birlar xonasidagi raqamni chiqaruvchi dastur tuzing.
 Masalan: n = 25; Natija: 2, 5'''
 
# N = int(input('ikki xonali son kiriting = '))
# n_10 = N // 10
# n_1 = N % 10
# print(n_10, "o'nlar xonasi", n_1, "birliklar xonasdi")
 
''' 5. Ikki xonali son berilgan. Uning raqamlar yig'indisini aniqlovchi dastur
tuzing.
Masalan: n = 25; Natija 2+5=7'''

# N = int(input(' ikki xonali sonni kiriting = '))
# n_10 = N // 10
# n_1 = N % 10
# print('natija:',n_10 + n_1)


''' 6. Ikki xonali son berilgan. Uning raqamlar o'rni almashtirishdan hosil
bo'lgan sonni aniqlovchi dastur tuzing.
Masalan: n = 25; Natija: 52'''

# N = int(input(' ikki xonali sonni kiriting = '))
# n_10 = N //10
# n_1 = N % 10
# print('natija:', n_1 * 10 + n_10)

''' 7. Uch xonali son berilgan. Uning yuzlar xonasidagi raqamni aniqlovchi
dastur tuzing.
Masalan: N = 123; Natija: 1'''

# N = int(input(' uch xonali son kiriting = '))
# n_100 = N //100
# print(n_100)

''' 8. Uch xonali son berilgan. Oldin uni birliklar xonasidagi raqamni, so'ng,
o'nliklar xonasidagi raqamni chiqaruvchi dastur tuzing.'''

# N = int(input(' Uch xonali son kiriting = '))
# n_1 = N % 10
# n_10 = (N // 10 ) % 10

# print('birlik = ',n_1, 'onlik = ',n_10) 

''' 9. Uch xonali son berilgan. Uni raqamlar yig'indisini aniqlovchi dastur
tuzing.'''

# N = int(input(' uch xonali son kiriting = '))
# n_1 = N % 10
# n_10 = (N // 10 ) % 10
# n_100 = N //100
# print('natija = ', n_1 + n_10 + n_100)

''' 10. Uch xonali son berilgan. Uni raqamlarini teskari tartibda yozishdan
hosil bo'lgan sonni aniqlovchi dastur tuzing.
Masalan: n = 123; Natija: 321 '''

# N = int(input(' uch xonali son kiriting = '))
# n_1 = N % 10
# n_10 = (N // 10) %10
# n_100 = N // 100

# print('natija = ', n_1 * 100 + n_10 * 10 + n_100)

''' 11. Uch xonali son berilgan. Uni chapdan birinchi raqamini o'chirib
o'ng tarafiga yozishdan hosil bo'lgan sonni aniqlovchi dastur tuzing.
Masalan: n = 478; natija: 784'''

# N = int(input( ' uch xonali sonni kiriting = '))
# n_1 = N %10
# n_10 =  (N // 10) %10
# n_100 = N //  100
# print('natija = ', n_10 * 100 + n_1 * 10 + n_100)

'''12. Uch xonali son berilgan. Uni o'ngdan birinchi raqamini o'chirib,
chap tarafiga yozishdan hosil bo'lgan sonni aniqlovchi dastur tuzing.
Masalan: n = 473; natija: 347'''

# N = int(input(' uch xonali sonni kiriting  = '))
# n_1 = N % 10 
# n_10 = (N // 10) % 10
# n_100 = N // 100
# print(' natija = ', n_1*100 + n_100 *10 + n_10) 

''' 13. Uch xonali son berilgan. Uni o'nliklar xonasidagi raqam bilan
yuzliklar xonasidagi raqamni almashtirishdan hosil bo'lgan sonni
aniqlovchi dastur tuzing.
Masalan: n = 387; natija: 837'''

# N = int(input(' uch xonali sonni kirting = '))
# n_1 = N %10
# n_10 = (N // 10) % 10
# n_100 = N // 100
# print('natija = ', n_10*100 + n_100*10 +n_1)

'''14. Uch xonali son berilgan. Uni o'nliklar xonasidagi raqam bilan
birliklar xonasidagi raqamni almashtirishdan hosil bo'lgan sonni
aniqlovchi dastur tuzing.'''

# N = int(input(' uch xonali son kiriting = '))
# n_1 = N % 10
# n_10 = (N // 10) % 10
# n_100 = N // 100
# print(" natija = ",n_100 * 100 + n_1*10 + n_10 )

''' 15. 999 dan katta son berilgan. Uni yuzliklar xonasidagi raqamni
aniqlovchi dastur tuzing.
Masalan: n = 4783; natija 7'''

# N = int(input(' 999 dan katta son kiriting = '))
# n_100 = (N // 100) % 10
# print(n_100)

''' 16. 999 dan katta son berilgan. Uni mingliklar xonasidagi raqamni
aniqlovchi dastur tuzing.
Masalan: n = 4783; natija 4'''

# N = int(input(' 999 dan katta son kiriting = '))
# n_1000 = N // 1000
# print('Natija = ',  n_1000)

''' 17. Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab
qancha minut to'la o'tganini aniqlovchi dastur tuzing.
Masalan: 125; Natija: 2 min'''

# N = int(input(' sekund kiriting = '))
# M = N // 60
# print('natija = ', M)

''' 18. Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab
qancha soat to'la o'tanini aniqlovchi dastur tuzing.
Masalan: n = 3650; natija 1 soat'''

# N = int(input(' sekundni kiriting = '))
# S = N // 3600
# print('natija =', S, " soat")

''' 19. Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab
qancha minut va sekund o'tganini aniqlovchi dastur tuzing.
Masalan: n = 125; natija: 2 min 5 s.'''

# N = int(input(' sekundni kiriting = '))
# m = N // 60
# s = N %60
# print('natija = ', m , " min ", s, 'sekund' )

''' 20. Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab
soat, minut va sekund o'tganini aniqlovchi dastur tuzing.'''

# N = int(input('sekundni kiriting = '))
# S = N // 3600
# m = (N % 3600) // 60
# s = N % 60
# print("natija = ", S, ' soat', m,' minut', s, ' sekund')