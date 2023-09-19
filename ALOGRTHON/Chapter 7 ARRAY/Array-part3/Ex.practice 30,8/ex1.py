# Ex1 - Array string
arr = ['banana','coconut','mango','jackfruit']

#1 - Count letter each item (function)
# [6,7,5,9]
# newarr = []
# def countLetter(item):
#     n = len(item)
#     newarr.append(n)
#     return newarr
# for i in range(len(arr)):
#     res = countLetter(arr[i])
# print(newarr)

# word = ''
# i = 0
# newarr = []
# while i < len(arr):
#     word = arr[i]
#     n = len(word)
#     newarr.append(n)
#     i +=1
# print(newarr)


#2 - Reverse string in list (function)
# ['ananab', 'tunococ', ...]
# def reverseLetter(value,newarr):
#     res = ''
#     for i in range(len(value)):
#         res += value[-1-i]
#     newarr.append(res)
#     return newarr
# word = ''
# newarr = []
# for j in range(len(arr)):
#     word = arr[j]
#     result = reverseLetter(word,newarr)
# print(newarr)


# i = 0
# word = ''
# while i < len(arr):
#     word= arr[i]
#     res = ""
#     for j in range(len(word)):
#         res += word[-1-j]
#     arr[i] = res
#     i += 1
# print(arr)


#3 - Count letter "n" in list (function)
# [2, 1, 1, 0]

# def countLetter(value,newList):
#     count = 0
#     for i in range(len(value)):
#         if value[i] == 'n':
#             count +=1
#     newList.append(count)
#     return newList
# newList = []
# word = ''
# for i in range(len(arr)):
#     word = arr[i]
#     res = countLetter(word,newList)
# print(newList)


# i = 0
# word = ''
# newarr = []
# while i < len(arr):
#     word = arr[i]
#     j = 0
#     count = 0
#     while j < len(word):
#         if word[j] == 'n':
#             count +=1
#         j +=1
#     newarr.append(count)
#     i +=1
# print(newarr)

#4 - Get last letter in each item (function)
# ['a', 't', 'o', 't']


# def getLastLetter(value,newarr):
#     n = value[len(value)-1]
#     newarr.append(n)
#     return newarr
# newarr = []
# word = ''
# for i in range(len(arr)):
#     word = arr[i]
#     res = getLastLetter(word,newarr)
# print(newarr)


# i = 0
# word = ''
# index = ''
# newarr = []
# while i < len(arr):
#     word = arr[i]
#     index = word[len(word)-1]
#     newarr.append(index)
#     i += 1
# print(newarr)



#5 - Add new fruit to list (function)
# function name: addNewFruit(arr, newFruit)
# ['banana','coconut','mango','jackfruit', 'orange']
# def addNewFruit(arr,newFruit):
#     arr.append(newFruit)
#     return arr
# newFruit = 'orange'
# print(addNewFruit(arr ,newFruit))


#6 - Concate first text together
# bcmj
# i = 0
# string = ''
# word = ''
# while i < len(arr):
#     word = arr[i]
#     string += word[0]
#     i +=1
# print(string)