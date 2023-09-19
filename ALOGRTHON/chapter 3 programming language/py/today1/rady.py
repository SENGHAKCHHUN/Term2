# number = 12.5
# z = int(number)
# print(z)
# print(type(z))

# number = "string"
# z = float(number)
# print(z)

# number = "hello"
# number = "10"
# print(float(number))

# number = "3"
# number = int(number)
# for i in range(number):
#     if number < 3:
#         print("Small")
#     else:
#         print("Greater")
# n = input("khmer")
# print(type(n))

# n = int(input())
# x = input()
# z = ""
# for i in range(n):
#         z = z + x
# print(z)

# n1 = int(input())
# n2 = int(input())
# letter = input()
# result = ""
# for i in range(n1):
#     result = result + letter[0]
# for i in range(n2):
#     result = result + letter[1]
# print(result)




# ex1
# text1 = "my name is "
# name = input("What is your name? ")
# text2 = "my age is "
# age = input("how old are you ? ")
# sentence = text1 + name + text2 + age
# print(sentence)
# print(text1, name, text2, age)

# ex3
# nb1 = "3"
# for i in range(nb1):
#     print("hello" + True)

# ex5
# x = 0
# condition1 = x = 4
# condition2 = False
# print(condition1)
# while condition1:
    # print(condition2)
#     x += 1
# condition2 = "True"
# print(condition2)
# print(type(condition1))
# print(type(condition2))

# ex6
# myNumber = 8
# newNumber = myNumber*2
# print(newNumber)
# print(type(myNumber))

# ex7
# text = "bouh"
# if text == "bouh":
#     print("yes")
# elif len(text) < 4:
#     print("maybe")
# else:
#     print("no")
# print(type(text))

# ex8
# number = 4.5
# integer = int(number)
# text = str(number)
# boolean = bool(number)
# print(type(number))
# print(type(integer))
# print(type(text))
# print(type(boolean))

# text = "Ture"
# boolen = bool(text)
# string = str(boolen)
# condition1 = string < text
# condition2 = text == boolen
# print(condition1)
# print(condition2)
# print(type(condition2))

# nb1 = float (True)
# nb2 = int(False)
# print(nb1, nb2)

# number = 5
# status = True
# for i in range(number):
#     if status and number > 3:
#         print(True)
#     else:
#         status = False
#     number = number - 1

# text = input()[::-1]
# print(text)

# text = input()
# result = ""
# for i in range(len(text)):
#     if text[i] == 'A':
#         result = result +"*"
#     elif text [i] == 'a':
#         result = result + "@"
#     else:
#         result = result + text[i]
# print(result)

# text = input()
# result = ""
# for i in range(len(text)):
#     if text[i] == ' ':
#         result = result +""
#     else:
#         result = result + text[i]
# print(result)

# text = input()
# A = 0
# B = 0
# for i in range(len(text)):
#     if text[i] == 'A':
#         A = A + 1
#     elif text[i] == 'B':
#         B = B + 1
# print(A)
# print(B)

# text = input()
# result = ""
# for i in range(len(text)):
#     result += text[len(text)-1-i]
# print(result)


# number = int(input())
# if number < 7:
#     print("Good")
# else:
#     print("Bad")

# number = int(input())
# while number<7:
#     print("Good")
# else:
#     print("bad")

# n = int(input(">"))
# factorial = 1
# result =""
# for i in range(n):
#     number = i + 1
#     factorial = factorial * number
#     if i == n - 1:
#         result += str(number)
#     else:
#         result +=str(number)+" x "
# print(result + " = "+ str(factorial))


# number = input()
# Number = ""
# secondNumber = ""
# isStop = False
# for i in range(len(number)):
#     if number[i] != '|' and not isStop:
#         Number += number[i]
#     else:
#         if isStop:
#             secondNumber += number[i]
# if int(Number) > int(secondNumber):
#     print("Yes")
# else:
#     print("No")


# text = input()
# isStop = True
# i = 0
# while i < len(text) and isStop:
#     if text[i]=='o':
#         result = i
#         isStop = False
#     else:
#         result = "-1"
#     i +=1
# print(result)




# text = input()
# isFalse = False
# isSeven = True
# for i in range(len(text)):
#     if text[i] != "0" and not isFalse:
#         result = -1
#         isFalse = True
#     elif isSeven and isFalse:
#         result = i
# print(result)

text = input()
result = -1
is_finished = False
for index in range(len(text)) :
    letter = text[index]
    if letter == "K" and is_finished:
        result = index
        is_finished = True
print(result)

