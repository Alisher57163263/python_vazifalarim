# for i in range(1,5):
#     print(i, end = " : ")
#     for j in range(1,7):
#         print(j, end=" ")
#     print("\n")

# for i in range(2,10):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("\n")

# 3-misol

# n = int(input("n = "))

# for i in range(n):
#     for j in range(n):
#         if i + j == n - 1 :
#             print(" * " , end= " ")
#         else:
#             print(" ", end = "    ")
#     print("\n")
   
# 4 - misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n - 1:
#             print(" * ", end= " ")
#         else:
#             print("   ", end=" ")
#     print("\n")

# b)

# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")
   
#  5- misol

# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n -1 or i == n // 2 :
#             print(" * ", end=" ") 
#         else:
#             print("   ", end=" ")
#     print(" \n")        

# b) 
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == n // 2:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print(" \n ")

# 6-misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n - 1 or j + i == n -1:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")

# b)
# n = int(input("n = "))
# for i  in range(n):
#     for j in range(n):
#         if j == 0 or j == n - 1 or j == i:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")

# 7-misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")

# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i <= j :
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")        

#  8 - misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for  j in range(n):
#         if i + j >= n - 1:
#             print(" * ",end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")
    
# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or i == j:
#             print(" * ", end=" ")
#         else:
#             print("   ",end=" ")
#     print("\n")

# 9 - misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if j == 0 or i == n - 1:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")
    
# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == n - 1:
#              print(" * ", end=" ") 
#         else:
#             print("   ", end=" ")
#     print("\n")
   
#    10 - misol
#  a) 
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or j == n - 1 or n - 1 == i:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")  

# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or j == n - 1 or i == n - 1 or j == n // 2 or i == n // 2:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")

# 11 misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if not (i == 0 or j == 0 or j == n - 1 or i == n - 1 or j == n // 2 or i == n // 2):
#             print(" * ", end=" ")
#         else:
#             print("  ", end=" ")
#     print("\n")

# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if not (j == 0 or i == 0 or i == n - 1 or j == n-1 or j == n // 2 or i == n//2) or i == 0 or i == n - 1:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")

# 12 - misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if j == 2 and 1<= i <=3 or i == 2 and 1<= j <=3:
#             print(" * ", end=" ")
#         else:
#             print("   ",end=" ")
#     print("\n")

# b) xato!!!
n = int(input("n = "))
for i in range(n):
    for j in range(n):
        if (j == 0 or j == n -1) or  (i % 2 == 1 and j % 2 ==1) :
            print(" * ",end=" ")
        else:
            print("   ", end=" ")
    print("\n")
# 13 - misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if j % 2 == 0:
#             print(" * ",end=" ")
#         else:
#             print("  ", end=" ")
#     print("\n")

# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i % 2 == 0:
#             print(" * ", end=" ")
#         else:
#             print("  ",end=" ")
#     print("\n")
# 14 -misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n-1 or (i % 2 == 0 and j % 2 == 0):
#             print(" * ", end="  ")
#         else:
#             print("  ", end="  ")
#      print("\n")

# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if (i + j) % 2  == 1 :
#             print(" * ",end="  ")
#         else:
#             print("   ", end="  ")
#     print("\n")

# 15 misol
# a)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == 1 or i == n-2 or j == 1 or j == n-2:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
#     print("\n")        

# b)
# n = int(input("n = "))
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             print(" * ", end="  ")
#         else:
#             print("  ",end="  ")
#     print("\n")

