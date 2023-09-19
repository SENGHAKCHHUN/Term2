# Ex3 - Array number
arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
#1 - Reverse array
# array = []
# for i in range(len(arr)):
#     array.append(arr[-1-i])
# print(array)


#2 - Remove duplicate value
# def removeDuplicate(value,array):
#     bool = True
#     for i in range(len(array)):
#         if array[i] == value:
#             bool = False
#     return bool
# newarr = []
# for i in range(len(arr)):
#     if removeDuplicate(arr[i],newarr):
#         newarr.append(arr[i])
# print(newarr)


#3 - replace numebr > 3 with 0
# for i in range(len(arr)):
#     if arr[i] == 3:
#         arr[i] = 0
# print(arr)


#4 - Find average of odd number
# sum = 0
# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         sum += arr[i]
# sum = sum / len(arr)
# sum = int(sum)
# print(sum)


#6 - remove number 8, 9, 10
# def removeNumber(value,array):
#     index = None
#     for i in range(len(array)):
#         if array[i] == value:
#             index = i
#     array.pop(index)
#     return array
# arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
# res = (removeNumber(8,arr))
# res = (removeNumber(9,arr))
# print(removeNumber(10,arr))
# ----------
# for i in range(len(arr)):
#     print(arr[-1-i])



arr = [10,5,2,7,9,2,5]
i = 0
index = None
bool = False
while i < len(arr) and not bool:
    if arr[i] == 2:
        index = i
        bool = True
    i +=1
print(index)





