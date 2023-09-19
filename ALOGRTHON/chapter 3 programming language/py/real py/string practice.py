# ex1
# n = 0
# if n > 10:
#     print("Hello")
# else:
#     print("OK")
# ex1
# for i in range(10):
#     print("Hello")

# ex2
# n = int(input())
# for i in range(n):
#     print("Hello")

# ex6
# n1 = int(input())
# n2 = int(input())
# sum = n1 + n2
# print("Result:" + str(sum))

# ex7
# n1 = int(input())
# n2 = int(input())
# sum = n1 * n2
# print("Result:" + str(sum))

# ex8
# sum = 0
# n = int(input())
# sum = n*n
# print("Result:" + str(sum))

# ex9
# n = int(input())
# if n % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# ex10
# n = int(input())
# if n < 0:
#     print("Negative number")
# elif n > 0:
#     print("Positive number")
# else:
#     print("Center number")

# ex10
# text = input()
# n = len(text)
# for i in range(n):
#     print(i)
# ex11
# text =input()
# number = len(text)
# for i in range(number):
#     result= text [i]
#     print(result)

# ex12
# text = (input())
# n = len(text)
# result =""
# for i in range(n):
#     result = result + ("M")
# print(result)

# ex13
# result = 0
# text =input("enter number")
# n = len(text)
# for i in range(n):
#     if text[i] == 'a':
#         result = result + 1
# if  result == 0:
#     print("A not found")
# print(result, "A in text")

# ex14
# n = int(input("enter"))
# y = int(input("enter"))
# while n < (y - 1):
#     n = n + 1
#     print(n)

# ex15
# x = input("enter number")
# y = input("enter number")
# z = input("enter number")
# if x > y > z:
#     print(str(x) , "is bigger than other")
# elif x < y > z:
#     print(str(y) , "is bigger than other")
# else:
#     print(str(z), "is bigger than other")

# ex16
# sum = 0
# a = int(input("enter"))
# b = int(input("enter"))
# c = int(input("enter"))
# d = int(input("enter"))
# e = int(input("enter"))
# sum = a + b + c + d + e
# print("sum:", sum)

# ex17
# number = 0
# while number != 7:
#     number = int(input())
# print("Good bye")

# ex18
# number = 0
# while number !=7:
#     number = int(input())
#     print("Try again")
# print("Good bye")
# ex19
# sum = ""
# number = int(input())
# for i in range(number):
#     sum += "x"
#     print(sum)

# ex20
# sum = ""
# number = int(input())
# for i in range(number):
#     sum += "x"
# for i in range(number):
#     print(sum)
#     sum = sum[:-1]

# ex21
# text = input()
# number = len(text)
# result=""
# for i in range(number):
#     if text[i] == 'a':
#         result += "*"
#     elif text[i] != 'a':
#         result += text[i]
# print(result)

# ex22
# text = input()
# number = len(text)
# result=""
# for i in range(number):
#     if text[i] == 'a':
#         result += "*"
#     elif text[i] == 'b':
#         result += "#"
#     elif text[i] != 'a' or 'b':
#         result += text[i]
# print(result)

# ex11
# text = input()
# for i in range(len(text)):
#     print(text[i])

# ex12
# text = input()
# result = ""
# for i in range(len(text)):
#     result = result + "M"
# print(result)
# ex12
# text = input()
# n = len(text)
# result = ""
# for i in range(n):
#     result = result + "M"
# print(result)

# ex13
# text = input()
# n = len(text)
# result = int()
# for i in range(n):
#     if text[i] == 'a'or text[i] == 'A':
#         result += 1
# if result > 0:
#     print(str (result) + "A in text")
# else:
#     print("A no found")

# ex14
# x = int(input("enter"))
# y = int(input("enter"))
# while x < y-1:
#     x = x + 1
#     print(x)

# ex15
# n1 = input()
# n2 = input()
# n3 = input()
# if n1 > n2 and n1 > n3:
#     print(str(n1) , "is bigger than other")
# elif n1 < n2 and n2 > n3:
#     print(str(n2) , "is bigger than other")
# elif n1 < n3 and n2 < n3:
#     print(str(n3) , "is bigger than other")

# ex16
# sum = 0
# for i in range (5):
#     n = int(input())
#     sum = sum + n
# print("Sum:" + str(sum))

# ex17
# n = 0
# while n != 7:
#     n = int(input())
# print("Good night")

# ex17
# isSeven = False
# while not isSeven:
#     n = int(input())
#     if n == 7:
#         isSeven = True
# print("Good night")

# ex18
# isSeven = False
# while not isSeven:
#     n = int(input("enter"))
#     if n == 7:
#             isSeven = True
#     else:
#         print("Try again")
# print("Good job")  

# ex19
# n = int(input())
# result=""
# for i in range(n):
#     for j in range(n-i):
#         result += "x" 
#     result += "\n"
# print(result)

# ex24
# text = input()
# print(text.upper())

# ex25
# text = input("type word")
# count = 0
# for i in text:
#     if i.isupper():
#         count = count + 1    
# if count > 0:
#     print(count, "uppercase letter")
# else:
#     print("No uppercase letter")

# text = input()[::-1]
# print(text)


# text = "123"
# result =""
# for i in range(len(text)):
#     for j in range(int(text[i])):
#         result += "a"
#     result += "b"
# print(result)

# text = "123"
# result =""
# for i in range(len(text)):
#     for j in range(int(text[i])):
#         result += "a"
#         for K in range(2):
#             result += "b"
#     result += "c"
# print(result)
