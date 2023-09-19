# Ex1 - basic 1
# arr = ["banana","apple"]

#1 - How many "a" or "A" in list
# count = 0
# for i in range(len(arr)):
#     word = arr[i]
#     for j in range(len(word)):
#         if word[j] == 'a' or word[j] == 'A':
#             count +=1
# print(count)


#2 - Create new array store letter difference from A
# list = []
# bool = False
# for i in range(len(arr)):
#     word = arr[i]
#     for j in range(len(word)):
#         if word[j] == "a" or word[j] == "A":
#             bool = True
#         else:
#             list.append(word[j])
# print(list)
#   Output: ["b", "n", "n", "p", "p", "l", "e"]




# -----------------------------------
# Ex2 - basic 2
# arr = [2, 3, 4, 3, 2, 5, 3, 2, 5]

#1 - Square odd number in list
# for i in range(len(arr)):
#     if arr[i] %2 != 0:
#         arr[i] = arr[i] * arr[i]
# print(arr)



#2 - Filter list with dupplicate value
# arr.sort()
# array = []
# for i in range(len(arr)):
#     if arr[i-1] != arr[i]:
#         array.append(arr[i])
# print(array)



# def checkValue(value,array):
#     isUnique = True
#     for i in range(len(array)):
#         if value == array[i]:
#             isUnique = False
#     return isUnique
# newArr = []
# arr = [2, 3, 4, 3, 2, 5, 3, 2, 5]
# for i in range(len(arr)):
#     if checkValue(arr[i],newArr):
#         newArr.append(arr[i])
# print(newArr)
#    output: [2, 3, 4, 5]
# -----------------------------------




# Ex3 - basic 3
arr = [1, 0, 0, 1, 0]

#1 - Replace 0 with x
# for i in range(len(arr)):
#     if arr[i] == 0:
#         arr[i] = 'x'
# print(arr)
# 2 - Move 0 before 1
# arr.sort()
# print(arr)
start = arr[0]
i = 0
list = []
isTrue = False
for i in range(len(arr)):
    if start > arr[i]:
        start = arr[i]
for i in range(len(arr)):
    if start == arr[i]:
        list.append(arr[i])
        isTrue = True
    elif isTrue:
        list.append(arr[i])
print(list)

#   Output: [0, 0, 0, 1, 1]
# -----------------------------------