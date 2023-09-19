# Ex3 - Array
# arr = [6, 4, 3, 4]
#1 - Sum first index with last  index
# result = 10
# sum = 0
# sum = arr[0] + arr[len(arr)-1]
# print(sum)


#2 - Square all number (function)
# [36, 16, 9, 16]
# def squareNumber(value):
#     value *=value
#     return value
# value = 1
# arr = [6, 4, 3, 4]
# res = ''
# for i in range(len(arr)):
#     res = squareNumber(arr[i])
#     arr[i] = res
# print(arr)



#3 - Remove duplicate from list (function)
# [6, 3, 4]
# def checkValue(value,newl):
#     isTrue = True
#     for i in range(len(newl)):
#         if value == newl[i]:
#             isTrue = False
#     return isTrue
# arr = [6, 4, 3, 4]
# newl = []
# for i in range(len(arr)):
#     if checkValue(arr[i],newl):
#         newl.append(arr[i])
# print(newl)



#4 - create 2D array follow number in list
newlist = []
arr = [6, 4, 3, 4]
number = 0
res = ''
for i in range(len(arr)):
    number = arr[i]
    newarr = []
    for j in range(number):
        newarr.append(j+1)
    newlist.append(newarr)
    res = ''
print(newlist)
# [
#   [1, 2, 3, 4, 5, 6],
#   [1, 2, 3, 4]
#   [1, 2, 3],
#   [1, 2, 3, 4]
# ]