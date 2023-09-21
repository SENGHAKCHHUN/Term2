# arr = [{'money' : [100,123,145]},{'money' : [10,14,200]}]
# newarr = []
# for key in arr:
#   for value in key:
#     for i in range(len(key[value])):
#       newarr.append(key[value][i])
# obj = {}
# obj['number'] = newarr
# print(obj)




# ex1
# def findTwoLetter(string):
#     count = 0
#     for i in range(len(string)):
#         if string[i] == 'a':
#             count += 1
#     if count == 2:
#         isTrue = True
#     else:
#         isTrue = False
#     return isTrue
# arr = eval(input())
# list = []
# for h in range(len(arr)):
#     if findTwoLetter(arr[h]):
#         list.append(arr[h])
# print(list)




# ex2
# def reverseText(string):
#     result = ''
#     for i in range(len(string)):
#         result += string[-1-i]
#     return result
# array = eval(input("enter arr "))
# list = []
# for i in range(len(array)):
#     word = reverseText(array[-1-i])
#     list.append(word)
# print(list)




# ex3
# arr = [
#     {'name': 'Nit', 'subject': 'Algorithm', 'score': 10},
#     {'name': 'visal', 'subject': 'Pl', 'score': 80},
#     {'name': 'Dyna', 'subject': 'Algorithm', 'score': 91},
#     {'name': 'Sreymon', 'subject': 'Algorithm', 'score':50},
#     {'name': 'Virak', 'subject': 'English', 'score':50},
#     {'name': 'Khid', 'subject': 'Algorithm', 'score':70}
# ]
# count = 0
# res = ''
# for i in range(len(arr)):
#     if arr[i]["subject"] == "Algorithm":
#         if arr[i]['score'] < 50:
#             count +=1
#             res += arr[i]['name']+' '
# print(str(count) + ' student failed alogorithm: ' + res)




# array1 = [
#     {"subject": "html", "class": "WEP-B", "teacher-id": 45},
#     {"subject": "html", "class": "WEP-A", "teacher-id": 36},
#     {"subject": "Algorithm", "class": "WEP-D", "teacher-id": 36}
# ]
# array2 = [
#     {"teacher-id": 36, 'first-name': 'rady', 'last-name': 'Y'},
#     {"teacher-id": 45, 'first-name': 'ronan', 'last-name': 'The best'}
# ]
# count = 0
# for i in range(len(array1)):
#     if array1[i]['subject'] == 'Algorithm':
#         id = array1[i]['teacher-id']
#         for j in range(len(array2)):
#             if array2[j]['teacher-id'] == id:
#                 print(array2[j]['last-name'])
#                 count +=1
# if count == 0:
#     print('No teacher in algorithm subject')




# sala = {'bmc': 128 , 'st': 100, 'kaka': 1}
# min = sala['bmc']
# for key in sala:
#     if sala[key] < min:
#         min = sala[key]
# print(min)




# arr = ['banana','apple','pineapple']
# newarr = []
# for i in range(len(arr)):
#     newarr.append(arr[-1-i])
# print(newarr)




# def reverseWord(word):
#     res = ''
#     for i in range(len(word)):
#         res += word[-1-i]
#     return res
# for j in range(len(arr)):
#     arr[j] = reverseWord(arr[j])
# print(arr)




# newarr = []
# for vor in range(len(arr)):
#     newarr.append(reverseWord(arr[-1-vor]))
# print(newarr)




# arr = [
#     [1,2,3,4],
#     [4,5,6,6],
#     [7,8,9,9]
# ]
# i = 0
# sum = 0
# row = len(arr)
# col = len(arr[0])  
# for i in range(col):
#     if i == 3:
#         for j in range(row):
#             sum += arr[j][i]
#         print(sum)




# new = []
# for i in range(len(arr)):
#     sum = 0
#     for j in range(len(arr[i])):
#         sum += arr[i][j]
#     new.append(sum)
# print(new)
        
def checkValue(word,arr2):
    res = ''
    for i in range(len(word)):
        if word[i] == arr2[0]:
            res += arr2[1]
        else:
            res += word[i]
    return res       
array1 = ['banana', 'coconut', 'mango']
arr2 = ['a','*']
list = []
for i in range(len(array1)):
    list.append(checkValue(array1[i],arr2))
print(list)
