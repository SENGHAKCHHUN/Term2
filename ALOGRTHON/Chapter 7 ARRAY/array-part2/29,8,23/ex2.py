# Ex5 - Array (While loop only)
arr = ['A','A','B','B','C','A','C']
#1 - Create to new list to remove duplicate value
# def checkValue(number,newarr):
#     isBool = True
#     i = 0
#     while i < len(newarr):
#         if number == newarr[i]:
#             isBool = False
#         i += 1
#     return isBool
# newarr = []
# j = 0
# while j < len(arr):
#     if checkValue(arr[j],newarr):
#         newarr.append(arr[j])
#     j +=1
# print(newarr)



#2 - If A = 10, B = 20, C = 30 how many value in list in total
# i = 0
# sum = 0
# while i < len(arr):
#     if arr[i] == 'A':
#         sum += 10
#     elif arr[i] == 'B':
#         sum += 20
#     elif arr[i] == 'C':
#         sum += 30
#     i += 1
# print(sum)


#3 - Filter new list and keep letter "A" only
# newArr = []
# i = 0
# while i < len(arr):
#     if arr[i] == 'A':
#         newArr.append(arr[i])
#     i += 1
# print(newArr)




# Ex6 - Array (While loop only)
# arr = [1, 10, 168, 190, 2024, 120393]
#1 - Remove 2024 from list
# i = 0
# index = 0
# while i < len(arr):
#     if arr[i] == 2024:
#         index = arr[i]
#     i +=1
# arr.remove(index)
# print(arr)



#2 - How many degit from each item
# i = 0
# newArr = []
# while i < len(arr):
#     number = str(arr[i])
#     n = len(number)
#     newArr.append(n)
#     i +=1
# print(newArr)
# [1, 2, 3, 3, 4, 6]





#3 - replace all item that have degit greater than 3 by 100
# i = 0
# while i < len(arr):
#     if arr[i] > 3:
#         arr[i] = 100
#     i +=1
# print(arr)

# [1, 10, 100, 100, 100, 100]