# Ex6 - Array
# arr = ['banana','coconut','mango','Jackfruit','orange','apple']
#1 - Reverse only text contain 1 letter A
# def reverseText(arr):
#     result = ''
#     for h in range(len(arr)):
#         result+= arr[-1-h]
#     return result
# def checkLetterA(arr):
#     bool = False
#     count = 0
#     for j in range(len(arr)):
#         if arr[j] == 'a':
#             count +=1
#     if count == 1:
#         bool = True
#     else:
#         bool = False
#     return bool
# newlist = []
# for i in range(len(arr)):
#     if checkLetterA(arr[i]):
#         res = reverseText(arr[i])
#         newlist.append(res)
#     else:
#         newlist.append(arr[i])
# print(newlist)



#2 - Count letter A in text
# [3, 0, 1, 1, 1, 1]
# def countLetterA(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == 'a':
#             count +=1
#     return count
# list = []
# for i in range(len(arr)):
#     list.append(countLetterA(arr[i]))
# print(list)


#3 - Replace letter A with * in text   

arr = ['banana','coconut','mango','Jackfruit','orange','apple']
newArray = []
for i in range(len(arr)):
    newString = ""
    for j in range(len(arr[i])):
        if arr[i][j] == 'a':
            newString+= '*'
        else:
            newString+= arr[i][j]
    newArray.append(newString)
print(newArray)



