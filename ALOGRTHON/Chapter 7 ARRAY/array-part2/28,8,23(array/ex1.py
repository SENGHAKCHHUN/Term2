# Ex1 - Array string
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
#1 - Remove duplicate name from list
# def checkValue(value,listNumber):
#     bool = True
#     for i in range(len(listNumber)):
#         if value.upper() == listNumber[i].upper():
#             bool = False
#     return bool
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# listNumber = []
# for i in range(len(arr)):
#     if checkValue(arr[i],listNumber):
#         listNumber.append(arr[i])
# print(listNumber)



#2 - Reverse only "mengheang" name in list
# def checkword(word):
#     res = ''
#     for j in range(len(word)):
#         res += word[-1-j]
#     print(res)
#     return res
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# for i in range(len(arr)):
#     if arr[i] == 'mengheang':
#         arr[i] = checkword(arr[i])
# print(arr)


#3 - Add "Ronan" to first index
# arr.insert(0,'Ronan')
# print(arr)

# 4 - Create new list with number of character in list
# [4, 3, 9, 4, 3]
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# list = []
# for hak in range(len(arr)):
#     n = len(arr[hak])
#     list.append(n)
#     n = 0
# print(list)



#5 - Create new list with letter "a", "e", "i", "o", "u"
# ['a','o', 'e', 'e', 'a', 'a', 'o']
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# list = []
# for hak in range(len(arr)):
#     word = arr[hak]
#     for mo in range(len(word)):
#         if word[mo] == 'a' or word[mo] == 'e' or word[mo] == 'i' or word[mo] == 'o' or word[mo] == 'u':
#             list.append(word[mo])
# print(list)




#6 - Count number of 'A' in list
# [1, 0, 1, 1, 0]
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# count = 0
# list = []
# for hak in range(len(arr)):
#     word = arr[hak]
#     count =0
#     for mo in range(len(word)):
#         if word[mo] == 'a':
#             count +=1
#     list.append(count)
# print(list)





#7 - Keep name who start from letter "R" only

# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# list = []
# for i in range(len(arr)):
#     word = arr[i]
#     if word[0].upper() == 'R':
#         list.append(arr[i])
# print(list)

# def keepword(word):
#     if word[0].upper() == 'R':
#         return word
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# list = []
# for i in range(len(arr)):
#     word = arr[i]
#     if keepword(word):
#        list.append(word)
# print(list)

#8 - Remove "Mengheag" from list
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# index = 0
# for i in range(len(arr)):
#     if arr[i] == 'mengheang':
#         index = i
# arr.pop(index)
# print(arr)





#9 - Create nested array (Array 2D) from list
# [ ['R','a','d','y'], ['y','o','n'], ...]

# def newarray(word):
#     newArr = []
#     for j in range(len(word)):
#         newArr.append(word[j])
#     return newArr
# arr = ["Rady","yon","mengheang", "rady", "Yon"]
# list =[]
# for i in range(len(arr)):
#     word = arr[i]
#     list.append(newarray(word))
# print(list)

# -----------------------------------------------------