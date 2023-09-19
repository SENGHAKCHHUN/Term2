text = input()
result ='WRONG'
isFound = False
i = 0
while i < len(text)-1 and not isFound :
    if text[i] == 'a' and text[i+1] == 'b' and text[i+2] == 'c':
        result = 'OK'
    else:
        isFound = True  
    i+=2
print(result)      



# text = input()
# result = ""
# for i in range(int(text[0])):
#     result += text[1]
# print(result)
# result= ""
# for i in range(int(text[2])):
#     result += text[3]
# print(result)
# result =""
# for i in range(int(text[4])):
#     result += text[5]
# print(result)

# text = input()
# result = ""
# isStop = False
# i = 0
# while i < len(text) :
#     if text[i] != "'" and not isStop :
#         result += text[i]
#     elif text[i] == "'" and not isStop:
#         isStop = True
#     elif text[i] =="'":
#         isStop = False
#     i+= 1
# print(result)

# text = input()
# result = ""
# i=0
# while i<len(text)-1:
#     if text[i] != " ":
#         result += text[i]
#     else:
#         print(result)
#         result=""
#     i+=1

# number = int(input())
# result = ""
# for i in range(number):
#     for i in range(number):
#         result += "X"
#     result +="\n"
# print(result)

# n = int(input())
# result =""
# for i in range(n):
#     for j in range(n-i):
#         result += "X"
#     result+="\n"
# print(result)

# number = int(input())
# mode = input()
# result = False
# if (mode == "inside" and number>= 1 and number <=10) or (mode == "outside" and number<1 and number>10):
#     result = True
# print(result)



# value = input()
# result = ""
# result1 = ""
# isFound = False
# isStop = False
# for i in range(len(value)):
#     if value [i] != "'" and not isFound:
#         result += value[i]
#     elif value [i] == "'" and not isStop:
#         isFound = True
#     elif value[i] == "'" and value[i+1] == " ":
#         isFound = False
#     else:
#         result1+=value[i]
#         isStop = True
# print(result)
# print(result1)




# # ______step 1_______
# value = input()
# sum = 0
# result = ""
# # _______step 2_______
# for i in range(len(value)):
#     # print(value[i])
#     # ______step 3_______
#     if value[i] != '6':
#         sum += int(value[i])
#     else:
#         result="6"
# if result == "6":
#     print(sum)
# else:
#     print("No number 6")


# ex4
# value = input()
# result = 0
# result1 = 0
# isStop = False
# i = 0

# # ____step2______
# while i < len(value)-1 and not isStop:
#     # print(value[i])
#     # ____step3____
#     if int(value[i]) < int(value[i+1]):
#         result = value[i]
#     elif int(value[i]) > int(value[i+1]):
#         result1 = value[i]
#         isStop = True
#     i+=1
# print(result1 , result)




# text = input()
# small = int(text[0])
# big = 0 
# for i in range(len(text)):
#     if int(text[i]) < small:
#         small = int(text[i])
#     elif int(text[i]) > small and int(text[i]) > big:
#         big = int(text[i])
# print(big , small)


# size = int(input())
# number = int(input())
# result = ""
# symbol = input()
# if symbol == "Y" or symbol == 'X':
#     for i in range(size):
#         for i in range(number):
#             for i in range(size):
#                 result += symbol
#             result+=" "
#         result +="\n"
# else:
#     result = "symbol error"
# print(result)

value = int(input())
result = 0
isStop = False
for i in range(value):
    number = int(input())
    if number != 7 and not isStop:
        result += number
    else:
        isStop = True
print(result)

