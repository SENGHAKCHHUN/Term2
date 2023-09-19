# Ex2 - Dictionary or object
studentList = [
  {'id': 1, 'name': 'dara', 'score': 90, 'province':'Phnom Penh'},
  {'id': 2, 'name': 'kaka', 'score': 60, 'province': 'Ratanakiri'},
  {'id': 3, 'name': 'bopha', 'score': 42, 'province': 'Siem Riep'},
  {'id': 4, 'name': 'chompa', 'score': 40, 'province': 'Battambang'},
  {'id': 5, 'name': 'chompey', 'score': 25, 'province': 'Siem Riep'},
  {'id': 6, 'name': 'romdul', 'score': 110, 'province': 'Kratie'}
]
#1 - who is come from "Battambang" ?
# for key in studentList:
#     if key['province'] == 'Battambang':
#         studentName = key['name']
# print(studentName)


#2 - How many student come from "Siem Riep"?
# count = 0
# for key in studentList:
#     if key['province'] == 'Siem Riep':
#         count +=1
# print(count)


#3 - How many student has score below 50?
# count = 0
# for key in studentList:
#     if key['score'] < 50:
#         count +=1
# print(count)


#4 - Who get highest score in list
# studentName = studentList[0]['name']
# score = studentList[0]['score']
# for key in studentList:
#     if key['score'] > score:
#         score = key['score']
#         studentName = key['name']
# print(studentName)


#5 - Who get lowest score in list
# studentName = studentList[0]['name']
# score = studentList[0]['score']
# for key in studentList:
#     if key['score'] < score:
#         score = key['score']
#         studentName = key['name']
# print(studentName)


#6 - Remove who come from "Battambang" from list
index =0
for i in range(len(studentList)):
    if studentList[i]['province'] == 'Battambang':
        index = i
studentList.pop(index)
print(studentList)