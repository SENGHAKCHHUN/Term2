# arr = [{'money' : [100,123,145]},{'money' : [10,14,200]}]
# for key in range(len(arr)):
#   for i in range (len(arr[key])):
#     print(arr[key][i])  

# for key in arr:
#     for l in key:
#         for i in range(len(key[l])):
#             print(key[l][i])

# arr = {}
# arr['money'] = 1
# arr['id'] = 10
# arr['name'] = 'senghak'
# arr['id'] = 0
# print(arr)

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


sala = {'bmc': 128 , 'st': 100, 'kaka': 1}
min = sala['bmc']
for key in sala:
    if sala[key] < min:
        min = sala[key]
print(min)

