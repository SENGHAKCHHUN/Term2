# n1 = int(input())
# n2 = int(input())
# letter = input()
# result= ""
# # result1= ""
# for i in range(n1):
#     result = result + letter[0]
# for i in range(n2):
#     result = result + letter[1]
# print(result)


# n1=int(input())
# n2=int(input())
# letter=input()
# result1=""
# result2=""
# for i in range(n1):
#     result1+=letter[0]
#     for i in range(n2):
#         result2+=letter[1]
# print(result1+result2)

# number = int(input())
# letter = input()
# result = ""
# for i in range(number):
#     result += letter
# print(result)

# text = input()[::-1]
# print(text)

# a = 10
# b = a
# print("b")

# text1 = "my"
# name = input("what")
# text2 = "my"
# age = input()
# sentence = text1 + name + text2 + age
# print(sentence)
# print(text1, name, text2, age)

# star= ""
# for i in range(10):
#     for j in range(i):
#         star+="*"
#     star+='\n'
# # print(star)

# # star= ""
# for i in range(10):
#     for j in range(10-i):
#         star+="*"
#     star+='\n'
# print(star)

# star= ""
# for i in range(10):
#     for j in range(i):
#         star+="*"
#     star+='\n'

# for i in range(10):
#     for j in range(10-i):
#         star+="*"
#     star+='\n'
# print(star)
# star= ""
# for i in range(10):
#     for space in range(10-i):
#         star =star+" "

#     for j in range(i):
#         star+="* "
#     star+='\n'

# print(star)
# star =""
# for i in range(10):
#     for space in range(10-i):
#         star = star +" "

#     for j in range(i):
#         star += str(i) +" "
#     star+='\n'

# print(star)

# star = ""
# for i in range(10):
#     for space in range(10 + i):
#         star+=" "
#     for j in range(1, 10 - i):
#         star += str(j) +" "
#     star += '\n '
# print(star)

# string = "AKKFDFSS"
# C =string + "KING"
# print (C)

# text = "GoodMorning"
# print(text[:])

# text = input()
# result = ""
# for i in range(len(text)):
#     result = result + text[i]
# print(text[i])


# text = input()
# result = ""
# for i in range(len(text)):
#     if text[i] == 'a':
#         result = result + "X"
#     elif text[i] == 'b':
#         result = result + "Y"
#     else:
#         result = result + text[i]
# print(result)

# mystring = "We Are Student"
# print(mystring[0:8:4])


# mystring = "welcomeToPNC"
# print(mystring[1: :3])

# n = input()
# sum = int()
# result =int()
# for i in range(len(n)):
#     if n[i] == 'a' or n[i] == 'A':
#         result = result + 1
#     elif n[i] == 'B' or n[i]=='b':
#         sum = sum + 1
# print("A" , result)
# print("B" , sum)


# number = int(input())
# while number != 10:
#     print("Try again")
#     number = int(input())
# print("You won")


# number = input()
# n = len(number)
# sum = 0
# for i in range(n):
#     if number[i] >=8:
#         sum+= int(number[i])
# print(sum)


# n=int(input())
# result =""
# for i in range(n):
#     result += +"X"
# for j in range(n):
#     print(n:-1)


# n = input()
# lastIndex = len(n)-1
# if len[n] != 1:
#     sum = int(n[0]) + lastIndex
# sum == n
# print (sum)

# n = input()
# sum = 0

# if len(n) == 1:
#     sum+=int(n[0])
# elif len(n) == 2:
#     sum = int(n[0])+int([1])
# else:
#     sum = int(n[0]) + int(n[1]) + int(n[2])
# print(sum)

# number = input()
# n = len(number)
# sum = 0
# isTime = True
# i = 0
# while i < len(number) and isTime:
#     if i <=3:
#         sum = sum+int(number[i])
#     else:
#         isTime = False
#     i = i + 1
# print(sum)

# x = input()
# n = len(x)
# if n == 1:
#     sum = int(n)
# elif n == 2:
#     sum = int(x[1]) + int(x[0])
# else:
#     sum = int(x[n-1]) + int(x[n-2]) + int(x[n-3])
# print(sum)

# number = input()
# if len(number) == 1:
#     sum = int(number)
# else:
#     # for i in range(len(number)):


# number = input()
# n = len(number)
# i = 0
# isTime = False
# while i < n and not isTime:
#         sum += int(number[i])
#         isTime = True
#     i = i + 1
# print(sum)

# text = input()
# n = len(text)
# result1 = ""
# result= ""
# for i in range(n):
#     if text[i].isupper():
#         result +=text[i]
#     else:
#         result1 += text[i]
# print(result, "is uppercase")


# text=input()
# result1=""
# result2=""
# for i in range(len(text)):
#     if text[i].isupper():
#         result1+=text[i]
#     else:
#         result2+=text[i]
# print(result1,"is uppercase")
# print(result2, "is lowercase")


# number = int(input())
# result = 100
# result  -= number
# print("it's", result,"far from 100")

# score = int(input())
# if score<50:
#     print("Grade F")
# elif score >=50 and score <=60:
#     print("Grade E")
# elif score >60 and score <= 70:
#     print ("Grade D")
# elif score >70 and score <=80:
#     print("Grade C")
# elif score >80 and score <=90:
#     print("Grade B")
# elif score >90 and score <= 95:
#     print("Grade A")
# elif score >95 and score <=100:
#     print("Grade A+")



# n = int(input())
# result = 100
# result -= n
# if n >100:
#     print("Number is bigger than 100")
# else:
#     print("It's" , result ,"is far from 100")