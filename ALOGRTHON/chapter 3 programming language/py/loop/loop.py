# ex1
# for i in range(1, 11):
#     for j in range(1, i+1):
#         print("*", end=" " )
#     print()

# ex2
# paragraph = str(input("enter"))
# countWord = 0
# countSentence = 0
# for i in range(len(paragraph)):
#     if paragraph[i] == ' ':
#         countWord = countWord + 1
#     if paragraph[i] == "." or paragraph[i] == "?" or paragraph[i] == "!":
#         countSentence = countSentence + 1
# print("______________________________")
# print("This is my paragraph space:" , countWord )
# print("This is the number of sentences:", countSentence)

# number = int(input("Enter"))
# result =""
# for i in range(number):
#     result = result + "*"
#     print(result)
# result = ""
# for i in range(10):
#     for j in range(i):
#         result+="*"
#     result+="\n"
# print(result)


# result=""
# for i in range(9):
#     for j in range(i):
#         result+=str(i)+" "
#     result+="\n"
# print(result)

# text = input()
# result = ""
# for i in range(len(text)):
#     for j in range(i+1):
#         result += text[j] + " "
#     result +="\n"
# print(result)


# result = ""
# for i in range(9):
#     for k in range(9-i):
#         result += " "
#     for j in range(i):
#         result += "* "
#     result += "\n"
# print(result)


# result = ""
# for i in range(9):
#     for k in range(9-i):
#         result += " "
#     for j in range(i):
#         result += "* "
#     result += "\n"
# for i in range(9):
#     for k in range(i):
#         result += " "
#     for j in range(9-i):
#         result += "* "
#     result += "\n"
# print(result)


# result = ""
# for i in range(9):
#     for k in range(i):
#         result += " "
#     for j in range(9-i):
#         result += "* "
#     result += "\n"
# for i in range(9):
#     for k in range(9-i):
#         result += " "
#     for j in range(i):
#         result += "* "
#     result += "\n"
# print(result)

# result = ""
# for i in range(10):
#     for j in range(9-i):
#         result += " "
#     for k in range(i):
#         result += "# "
#     result += "\n"
# print(result)

# result= ""
# for i in range(10):
#     for j in range(i):
#         result += " "
#     for k in range(9-i):
#         result += "* "
#     result += "\n"
# print(result)

result= ""
for i in range(5):
    for j in range(4-i):
        result += " "
    for k in range(i):
        result += "* "
    result += "\n"
for i in range(5):
    for j in range(i):
        result += " "
    for i in range(4-i):
        result+="* "
    result +="\n"
print(result)


