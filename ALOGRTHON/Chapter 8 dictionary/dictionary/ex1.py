# Ex1 - Dictionary or object
studentList = [
  {'id': 1, 'name': 'dara', 'age': 20},
  {'id': 2, 'name': 'kaka', 'age': 20},
  {'id': 3, 'name': 'bopha', 'age': 12},
  {'id': 4, 'name': 'chompa', 'age': 40},
  {'id': 5, 'name': 'chompey', 'age': 30},
  {'id': 6, 'name': 'romdul', 'age': 60},
]
#1 - who is younger in list
# for key in studentList:
#     younger = studentList[0]['age']
#     if key['age'] < younger:
#         younger = key['age']
#         res = key['name']
# print(younger)
# print(res)
        

#2 - who  is older in list
# for key in studentList:
#     if key['id'] == 1:
#         older = key['age']
#     if key['age'] > older:
#         older = key['age']
#         res = key['name']
# print(older)
# print(res)


#3 - how many student has the same age
# count = 0
# newarr = []
# for key in studentList:
#     newarr.append(key['age'])
# for i in range(len(newarr)):
#   res = newarr[i]
#   for j in range(len(newarr)):
#     if res == newarr[j] and i != j:
#       count += 1
# print(count)
        


#4 - how many student older than "kaka"
# age = studentList[1]['age']
# count = 0
# for key in studentList:
#     if key['age'] > age:
#         count +=1
# print(count)


#5 - remove student name "romdul" from the list
# index = 0
# for i in range(len(studentList)):
#     if studentList[i]['name'] == 'romdul':
#         index = i
# studentList.pop(index)
# print(studentList)

obj = {}
obj['id'] = 1
obj['name'] = 'cheap'
obj['province'] = 'kiki'
print(obj)


