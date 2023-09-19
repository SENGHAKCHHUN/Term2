# # ______ex1_______
# number = input()
# sum = 0
# for i in range(len(number)):
#     sum += int(number[i])
# print(sum)


# _or__

# n = input()
# sum = 0
# i = 0
# while i < len(n):
#     sum += int(n[i])
#     i += 1
# print(sum)


# # _________ex2_________
# number = input()
# sum = 0
# for i in range(len(number)):
#     if number[i] != '7' and number[i] != '9':
#         sum += int(number[i])
# print(sum)

# _or_

# number = input()
# i = 0
# sum = 0
# while i < len(number):
#     if number[i] != '7' and number[i] != '9':
#         sum += int(number[i])
#     i += 1
# print(sum)


# # ____ex3_______

# text = input()
# sum = 0
# for i in range(len(text)):
#     if text[i] == 'a' or text[i] == 'A':
#         sum += 10
#     elif text[i] == 'b' or text[i] == 'B':
#         sum += 5
#     elif text[i] == 'c' or text[i] == 'C':
#         sum += 3
#     else:
#         sum += 1
# print(sum)

# text = input()
# count_letter = 0
# count_number = 0
# for i in range(len(text)):
#     if text[i].isnumeric():
#         count_number += 1
#     else:
#         count_letter +=1
# print(str(count_letter) + " letter and " + str(count_number) + " number")

# ___Or___
# text = input()
# i = 0
# count_number = 0
# count_letter = 0
# while i < len(text):
#     if text[i].isnumeric():
#         count_number+= 1
#     else:
#         if text[i] != " ":
#             count_letter+=1
#     i +=1
# print(str(count_letter) + " letter and " + str(count_number) + " number")

# ___ex5____

# text = input()
# count_upper = 0
# count_lower = 0
# for i in range(len(text)):
#     if text[i].isupper():
#         count_upper +=1
#     elif text[i].islower():
#         count_lower +=1
# print(str(count_upper) + " uppercase and " + str(count_lower) +" lowercase" )


# ex6________
# text = input()
# result = ""
# isSix = False
# for i in range(len(text)):
#     if (text[i] == "d" or text[i] == "D") and not isSix:
#         result = "Yes"
#     else:
#         result = "No"
#         isSix = True
# print(result)

# ____or______
# text = input()
# isFound = False
# i = 0
# while i < len(text) and not isFound:
#     if text[i].upper() == "D":
#         result = "Yes"
#     else:
#         result = "No"
#         isFound = True
#     i +=1
# print(result)



# ___ex7_____

# text = input()
# result = ""
# isFound = False
# i = 0
# while i < len(text) and not isFound:
#     if text[i] == text[0]:
#         result = "Yes"
#     else:
#         result = "No"
#         isFound = True
#     i += 1
# print(result)

# # _______---or---______
# text = input()
# result = ""
# isHak = False
# for i in range(len(text)):
#     if text[i] != text[0]:
#         isHak = True
#         result = "No"
#     elif text[i] == text[0] and not isHak:
#         result = "Yes"
# print(result)

# ____ex8_____
# password = input("enter password")
# confirm = input("confirm password")
# if password == confirm:
#     print("Password correct!")
# else:
#     print("Password doesn't match")

# _____-ex9_____

text = input()
result = ""
isSign = False
for i in range(len(text)):
    if text[i] == '#':
        isSign = True
    elif isSign:
        for j in range(4):
            result += text[i]
    else:
        result+= text[i]
if  len(result) > 0:
    print(result)
else:
    print("No letter")

        

