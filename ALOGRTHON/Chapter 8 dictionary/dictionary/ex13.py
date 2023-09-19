# Ex3 - Dictionary or object
studentList = [
  {'id': 1, 'name': 'dara', 'salary': 250, 'province':'Phnom Penh'},
  {'id': 2, 'name': 'kaka', 'salary': 540, 'province': 'Ratanakiri'},
  {'id': 3, 'name': 'bopha', 'salary': 562, 'province': 'Siem Riep'},
  {'id': 4, 'name': 'chompa', 'salary': 330, 'province': 'Battambang'},
  {'id': 5, 'name': 'chompey', 'salary': 455, 'province': 'Siem Riep'},
  {'id': 6, 'name': 'romdul', 'salary': 550, 'province': 'Kratie'},
]
#1 - How many student from "Siem Riep"
# count = 0
# for key in studentList:
#     if key['province'] == 'Siem Riep':
#         count += 1
# print(count)


#2 - Find average of student salary
# sum = 0
# for key in studentList:
#     sum += key['salary']
# sum = sum / len(studentList)
# sum = int(sum)
# print(sum)


#3 - Who has higher salary in list
# hightSalary = studentList[0]['salary']
# for i in range(len(studentList)):
#     if studentList[i]['salary'] > hightSalary:
#         hightSalary = studentList[i]['salary']
# print(hightSalary)



#4 - Increase salary of Kaka to 670
# for key in studentList:
#     if key['name'] == 'kaka':
#         key['salary'] = 670
# print(studentList)


#5 - Rename "romdul" to "សុរិយាច័ន្ទ្រាមហាកញ្ញាបទុមកេសរនារីរ៍ត្ន"
# for key in studentList:
#     if key['name'] == 'romdul':
#         key['name'] = "សុរិយាច័ន្ទ្រាមហាកញ្ញាបទុមកេសរនារីរ៍ត្ន"
# print(studentList)


#5 -  Delete student has id number 5
# index = None
# for i in range(len(studentList)):
#     if studentList[i]['id'] == 5:
#         index = i
# studentList.pop(index)
# print(studentList)
