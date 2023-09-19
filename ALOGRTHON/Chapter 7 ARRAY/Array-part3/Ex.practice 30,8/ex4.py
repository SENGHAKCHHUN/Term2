# Ex1 - String
# text = "banana"
#1 - How many letter in string
# print(len(text))

#2 - How many letter "A" in string
# count = 0
# for i in range(len(text)):
#     if text[i] == "a":
#         count +=1
# print(count)


#3 - Reverse string
# res = ''
# for j in range(len(text)):
#     res += text[-1-j]
# print(res)

#4 - Convert all letter to uppercase except letter "A"
# res = ''
# for i in range(len(text)):
#     if text[i] != 'a':
#         res += text[i].upper()
#     else:
#         res += text[i]
# print(res)
# -----------------------



# Ex2 - Array
# arr = [1000, 200, 404, 500, 10]
#1 - How many degit of each item
# number = ''
# newList = []
# for i in range(len(arr)):
#     number = str(arr[i])
#     n = len(number)
#     newList.append(n)
# print(newList)
# [4, 3, 3, 3, 2]


#2 - Remove 404 from list
# index = 0
# for i in range(len(arr)):
#     if arr[i] == 404:
#         index = i
#         print(index)
# arr.pop(index)
# print(arr)


#3 - Reverse array
# [10, 500, 404, 200, 1000]
# newL = []
# for i in range(len(arr)):
#     newL.append(arr[-1-i])
# print(newL)



#4 - Sum only number with last degit is 0
# number = ''
# sum = 0
# for i in range(len(arr)):
#     number = str(arr[i])
#     if number[len(number)-1] == '0':
#         sum += int(number)
# print(sum)
# result: 1710

