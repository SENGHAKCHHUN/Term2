# text = input("text")
# result = ""
# i = 0
# isKhmer = False
# while i < len(text) and not isKhmer:
#     if text[i] == " " or text[i]==".":
#         print(result)
#         if result.upper() == "RADY":
#             isKhmer = True
#         result =""
#     else:
#         if text[i] != "?" and text[i]!=".":
#             result += text[i]
#     i +=1
# if result.upper() == "RADY":
#     print("Yes")
# else:
#     print("No")



# text = input()
# word = ""
# isSeven = False
# for i in range(len(text)):
#     if text[i] ==' ' or text[i] == '?' or text[i] == '.' or text[i] == ',' and not isSeven:
#         if word.upper() == "RADY":
#             isSeven = True
#         word = ""
#     elif text[i] != " " or text[i] != "?" or text[i] != "." or text[i] != ":" and not isSeven:
#             word+= text[i]
# if word.upper() == "RADY":
#     print("Yes")
# else:
#      print("No")

        
# text = input()
# result = ""
# for i in range(len(text)):
#     if text[i] != " ":
#         result += text[i]
#     elif text[i] == " ":
#         result += "\n"
# print(result)
    

# number = input()
# sum = 0
# for i in range(len(number)):
#     if number[i] != "3":
#         if number[i] != "7":
#             sum += int(number[i])
# print(sum)


 
# text = input()
# sum = ""
# isBig = False
# for i in range(len(text)):
#     if i == 0:
#         sum += text[i].upper()
#     elif text[i] == " ":
#         isBig = True
#         sum += text[i]
#     elif isBig:
#         sum += text[i].upper()
#         isBig = False
#     else:
#         sum += text[i]
# print(sum)



# text = input()
# result = ""
# isSix = False
# for i in range(len(text)):
#     if not isSix:
#         text[0].upper()
#         result += text[0]
#         isSix = True
#     elif text[i] != " ":
#         result += text[i]
#     elif text[i -1 ] == " ":
#         text[i].upper()
#         result += text[i]
# print(result)





# text = input()
# res = ""
# isSix = False
# sum = 0
# for i in range (len(text)):
#     if text[i].isnumeric():
#         res += text[i]
#         isSix = True
#     elif isSix:
#         sum += int(res)
#         isSix = False
#         res = ""
# if isSix:
#     sum += int(res)
# print(sum)



# text = input()
# res = 0
# for i in range(len(text)):
#     if text[i] != "3":
#         if text[i] != "8":
#             res += int(text[i])
# print(res)

# text = input()
# resA = 0
# resB = 0
# for i in range(len(text)):
#     if text[i] == "A":
#         resA += 10
#     elif text[i] == "B":
#         resB += 20
# sum = resA + resB
# print(sum)


name = input()
res = ""
for i in range(len(name)):
    for j in range(len(name)):
        if j >= i and j < len(name)-i:
            res += name[j]
        else:
            res += " "
    res += "\n"
print(res)