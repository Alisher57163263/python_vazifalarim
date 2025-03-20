# taqqoslash operatirlari

# n = int(input("n = "))
# m = int(input("m = "))
# s = n >m
# print(s)

''' 1. Rostlikka tekshiring. Berilgan son 5 ni 3 chi darajasiga teng.'''

# n = int(input("n = "))
# print(n == 5**3)

''' 2. Rostlikka tekshiring. Berilgan son 5 ni 3 chi darajasiga yoki 2-
darajasiga teng.'''

# n = int(input("n ="))
# print(n == 5**3 or n == 5**2)

''' 3. Rostlikka tekshiring. Berilgan a sonni 3 ga bo'linib 4 ga bo'linmaydi.'''

# a = int(input("a = "))
# print(a % 3 == 0 and a % 4 != 0)

''' 4. Rostlikka tekshiring. Ikkita 3 xonali a va b soni berilgan. Bularni
raqamlar yig'indisi teng.'''

# a = int(input("a = "))
# b = int(input("b = "))
# a_1 = a % 10
# a_10 = (a // 10) % 10
# a_100 = a // 100
# b_1 = b % 10
# b_10 = (b // 10) % 10
# b_100 = b // 100
# print(a_1 + a_10 + a_100 == b_1 + b_10 + b_100)

''' 5. Rostlikka tekshiring. Ikkita 4 xonali a va b soni berilgan. Bularni
raqamlar yig'indisini biri ikkinchisidan 2 marta katta'''

# a = int(input("a = "))
# b = int(input("b = "))
# a_1 = a % 10
# a_10 = (a // 10) % 10
# a_100 = (a // 100) % 10
# a_1000 = a // 1000
# a_sum = a_1 + a_10 + a_100 + a_1000 
# b_1 = b % 10
# b_10 = (b // 10) % 10
# b_100 =( b // 100) % 10
# b_1000 = a // 1000
# b_sum = (b_1 + b_10 + b_100 + b_1000)
# print(a_sum * 2 == b_sum or b_sum * 2 == a_sum  )

''' 6. Rostlikka tekshiring. Ikkita 4 xonali a va b soni berilgan. Bularni
raqamlar yig'indisini biri ikkinchisini kvadratiga teng.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) % 10
# a_4 = (a // 1000) 
# a_sum = a_1 + a_2 + a_3 + a_4
# b_1 = b % 10 
# b_2 = (b // 10) % 10
# b_3 = (b // 100) % 10
# b_4 = (b // 1000) 
# b_sum = b_1 + b_2 + b_3 + b_4
# print( a_sum ** 2 == b_sum or b_sum ** 2 == a_sum)

''' 7. Rostlikka tekshiring. Ikkita a va b soni berilgan. a soni 4 xonali b
soni 1 xonali. a sonini raqamlarini o'rta arifmetigi b soniga teng'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) % 10
# a_4 = (a // 1000)
# a_arf = (a_1 + a_2 + a_3 + a_4) // 4
# print(a_arf == b) 

''' 8. Rostlikka tekshiring. Ikkita a va b soni berilgan. a soni 4 xonali b
soni 1 xonali. a sonini raqamlarini o'rta arifmetigi b sonidan katta.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) % 10
# a_4 = (a // 1000)
# a_arf = (a_1 + a_2 + a_3 + a_4) // 4
# print(a_arf > b) 

''' 9. Rostlikka tekshiring. Ikkita a va b soni berilgan. a soni b sonidan 19
ga katta.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# print(a - b == 19)

''' 11. Rostlikka tekshiring. Ikkita a va b soni berilgan. Bu sonlardan biri
ikkinchisdan 23 ga katta.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# print( a - b >= 23 or b - a >= 23)

''' 12. Rostlikka tekshiring. Ikkita a va b soni berilgan. Shu sonlardan biri
ikkinchisidan 5 barabor ko'p'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# print(a // 5 == b or b // 5 == a)

''' 13. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini birlar
xonasidagi raqam 5 ga teng. '''

# a = int(input(' a = '))
# print(a % 10 == 5)

''' 14. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini birlar
xonasidagi raqam 5 ga yoki 9 teng.'''

# a = int(input(' a = '))
# print(a % 10 == 5 or a % 10 == 9)

''' 15. Rostlikka tekshiring. 4 xonali a soni berilgan. A sonini birlar va
minglar xonasi teng.'''

# a = int(input(' a = '))
# print(a % 10 == a // 1000)

''' 16. Rostlikka tekshiring. 4 xonali a soni berilgan. A sonini birlar va
minglar xonasidagi raqamlar yeg'indis o'nlar va yuzlar xonasidagi
raqamlarga teng.'''

# a = int(input(' a = '))
# print( a % 10 + a // 1000 ==  (a // 100) % 10 + (a // 10) % 10)

''' 17. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini chapdan
ham o'ngdan bir xil o'qiladi'''

# a = int(input(' a = '))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) 
# print(a_3 * 100 + a_2 * 10 + a_1 == a_1 * 100 + a_2 * 10 + a_3)

''' 18. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini hamma
raqami teng.'''

# a = int(input(" a = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) 
# print(a_1 == a_2 and a_3 == a_2 and a_1 == a_3)

''' 19. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini yuzlar
xonasidagi raqam eng kattasi.'''

# a = int(input(" a = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) 
# print(a_3 > a_1 and a_3 > a_2)

''' 20. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini birlar
xonasidagi raqam eng kattasi'''

# a = int(input(" a = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) 
# print(a_1 > a_2 and a_1 > a_3)

''' 21. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini o'nalar
xonasidagi raqam eng kichik.'''

# a = int(input(" a = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100)
# print(a_2 < a_1 and a_2 < a_3)

''' 22. Rostlikka tekshiring. 3 xonali a soni berilgan. A sonini
o'nalar xonasidagi birlar xonasidagi raqamdan 4 ga katta'''

# a = int(input(" a = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# print(a_2 - a_1 == 4)

''' 23. Rostlikka tekshiring. 2 xonali son berilgan. Berilgan sonni
raqmalarini yig'indisi ko'paytmasiga teng. '''

# a = int(input(" a = "))
# a_1 = a % 10
# a_2 = (a // 10)
# print(a_2 + a_1 == a_1 * a_2)


'''24. Rostlikka tekshiring. a soni berilgan. Berilgan son 4 xonali va uni
birlar xonasi bn minglar xonasidagi raqamlari yig'indisi o'nlar
xonasidagi va yuzlar xonasidagi raqamlar ko'paytmasiga teng.'''

# a = int(input(" a = "))
# a_1 = a % 10
# a_2 = (a // 10) % 10
# a_3 = (a // 100) % 10
# a_4 = (a // 1000)
# print(a_1 + a_4 == a_3 * a_2 )

''' 25. Rostlikka tekshiring. a , b , c , d sonlari berilgan b soni eng katta
va juft son.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# d = int(input(" d = "))
# print(b > a and b > c and b > d and b % 2 == 0)

''' 26. Rostlikka tekshiring. a , b , c , d sonlari berilgan. Berilgan sonlar
ichida faqat 2 tasi musbat.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# d = int(input(" d = "))
# print(a > 0 and b > 0 or  a > 0 and c > 0 or  a > 0 and d > 0 or b > 0 and c > 0 or b > 0 and b > 0 or c > 0 and d > 0)

''' 27. Rostlikka tekshiring. a , b , c , d sonlari berilgan. Berilgan sonlar
ichida faqat 3 tasi musbat'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# d = int(input(" d = "))
# print(a > 0 and b > 0 and c > 0 or a > 0 and b > 0 and d > 0 or a > 0 and c > 0 and d > 0 or b > 0 and c > 0 and d >0)

''' 28. Rostlikka tekshiring. 3 ta 5 xonali son berilgan. Berilgan sonlarni
raqamlar yig'indisi teng'''


# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# b_1 = b % 10 
# b_2 = (b // 10) % 10
# b_3 = (b // 100) % 10
# b_4 = (b // 1000) % 10
# b_5 =  b // 10000
# b_sum = b_1 + b_2 + b_3 + b_4 +b_5
# a_1 = a % 10 
# a_2 = (a // 10) % 10
# a_3 = (a // 100) % 10
# a_4 = (a // 1000) % 10
# a_5 =  a // 10000
# a_sum = a_1 + a_2 + a_3 + a_4 +a_5
# c_1 = c % 10 
# c_2 = (c // 10) % 10
# c_3 = (c // 100) % 10
# c_4 = (c // 1000) % 10
# c_5 =  c // 10000
# c_sum = c_1 + c_2 + c_3 + c_4 +c_5
# print(b_sum ==  a_sum and   c_sum == b_sum and a_sum == c_sum )

''' 29. Rostlikka tekshiring. 3 ta 3 xonali son berilgan. Berilgan sonlarni
raqamlar ko'paytmasi teng'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# b_1 = b % 10 
# b_2 = (b // 10) % 10
# b_3 = (b // 100) % 10
# b_k = b_1 * b_2 * b_3 
# a_1 = a % 10 
# a_2 = (a // 10) % 10
# a_3 = (a // 100) % 10
# a_k = a_1 * a_2 * a_3 
# c_1 = c % 10 
# c_2 = (c // 10) % 10
# c_3 = (c // 100) % 10
# c_k = c_1 * c_2 * c_3 
# print(b_k == a_k  and  b_k == c_k and a_k == c_k)

''' 30. Rostlikka tekshiring. 4 ta 3 xonali son berilgan. Kamida ulardan
bitta boshqasidan 2 barobar ko'p.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# d = int(input(" d = "))
# print(a * 2 == b or a * 2 == d or b * 2 == c or b * 2 == d or c * 2 == d or d * 2 == c or d * 2 == b or c * 2 == b or d * 2 == a or c * 2 == a or b * 2 == a)

''' 31. Rostlikka tekshiring. 4 ta son berilgan. Kamida 2 tasi toq.'''

# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))
# d = int(input(" d = "))
# print( a % 2 != 0 and b % 2 != 0 or a % 2 != 0 and c % 2 != 0 or a % 2 != 0 and d % 2 != 0 
#        or b % 2 != 0 and c % 2 != 0 or b % 2 != 0 and d % 2 != 0 or c % 2 != 0 and d % 2 != 0
#        )

'''32. Uchta son berilgan. Ulardan eng kattasini toping'''

# a = int(input(' a = '))
# b = int(input(' b = '))
# c = int(input(' c = '))
# d = (a * (a > b and a > c ) + b * (b > a and b > c ) + c * (c > a and c > b ) )
# print(d)
  