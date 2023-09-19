# Ex2 - Array number
# arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
#1 - Remove duplicate value in list by create new list
# def checkNumber(value,list):
#     isRun = True
#     for i in range(len(list)):
#         if value == list[i]:
#             isRun = False
#     return isRun
# arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
# newArr = []
# for i in range(len(arr)):
#     number = arr[i]
#     if checkNumber(number,newArr):
#         newArr.append(number)
# print(newArr)



#2 - Remove 8 from list
# arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]  
# for j in range(len(arr)):
#     if arr[j] == 8:
#         index = j
# arr.pop(index)
# print(arr)
        


#3 - Find average of this list
# sum = 0
# average = 0
# arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]  
# for i in range(len(arr)):
#     sum += arr[i]
# average = sum / len(arr)
# print(average)
    


#4 - Create new list with letter "A" following number in array
# newArray = []
# res = ''
# word = ''
# arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
# for i in range(len(arr)):
#     word = arr[i]
#     for j in range(word):
#         res += 'A'
#     newArray.append(res)
#     res = ''
# print(newArray)
# ['A','AAAAAAAAA','AAAAAAA', 'AAAAAAA',......]




# 5 - Sum only duplicate value
# def checkNumber(value,arr):
#     isRun = False
#     isTrue = True
#     j = 0
#     while j < len(arr) and not isRun:
#         if value == arr[j] and i != j:
#             isTrue = True
#             isRun = True
#         else:
#             isTrue = False
#         j +=1
#     return isTrue
arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
# newArray = []
# for i in range(len(arr)):
#     number = arr[i]
#     if  checkNumber(number, arr):
#         arr[i] += arr[i]
#         newArray.append(arr[i])
# print(newArray)
# [2,14]
# or___

# newArr = []
# for j in range(len(arr)):
#     for i in range(len(arr)):
#         if arr[i] == arr[j] and i != j:
#             arr[i] += arr[j]
#             newArr.append(arr[i])
# print(newArr)





#6 - Do NOT create new array remove all duplicate value
arr = [1, 9, 7, 7, 8, 3, 5,12, 1, 10]
number = ''
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j] == arr[i] and i != j:
            print(arr[i])
arr.remove(1)
arr.remove(1)
arr.remove(7)
arr.remove(7)
print(arr)



#7 - Replace all duplicate value with *
# def checkNumber(value,arr):
#     isRun = False
#     isTrue = True
#     j = 0
#     while j < len(arr) and not isRun:
#         if value == arr[j] and i != j:
#             isTrue = True
#             isRun = True
#         else:
#             isTrue = False
#         j +=1
#     return isTrue
# arr = [1, 9, 7, 7, 8, 3, 5, 12, 1, 10]
# newArray = []
# for i in range(len(arr)):
#     number = arr[i]
#     if  checkNumber(number, arr):
#         number = "*"
#         newArray.append(number)
#     else:
#         newArray.append(arr[i])  
# print(newArray)
    



#8 - Add value to 10 if value < 10
# newArr = []
# arr = [1, 9, 7, 7, 8, 3, 5, 12, 1, 10]
# for i in range(len(arr)):
#     if arr[i] < 10:
#         arr[i] = 10
#         newArr.append(arr[i])
#     elif arr[i] > 10:
#         newArr.append(arr[i])
# print(newArr)
# [10, 10, 10, 10, 10, 10, 12, 10, 10]




#9 - Add if value <= 5 and replace if value > 5 to make list store only 5 number
# [5, 5, 5, 5, 5, 5, 5, 5,5]
# for i in range(len(arr)):
#     if arr[i] <= 5:
#         arr[i] = 5
#     elif arr[i] > 5:
#         arr[i] = 5
# print(arr)