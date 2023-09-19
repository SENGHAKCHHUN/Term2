# Ex8
# Search students from list of array 2D
students = [
  ['bopha','2024A','kandal'],
  ['romdule','2024C','kompot'],
  ['kaka','2024C','Rathanakiri'],
  ['chompey','2024B','Siem Riep'],
  ['chompa','2024B','Battambang']
]
#1 - how many students from class A? B? and C?
def findNumber(array,value):
    count = 0
    for i in range(len(array)):
        sen = array[i]
        for j in range(len(sen)):
            if sen[j] == value:
                count +=1
    return count
students = [
  ['bopha','2024A','kandal'],
  ['romdule','2024C','kompot'],
  ['kaka','2024C','Rathanakiri'],
  ['chompey','2024B','Siem Riep'],
  ['chompa','2024B','Battambang']
]
print("student from class A " + str(findNumber(students,"2024A")))
print("student from class B " + str(findNumber(students,"2024B")))
print("student from class C " + str(findNumber(students,"2024C")))

#2 - Where kaka come from?
res = ''
for i in range(len(students)):
    sen = students[i]
    for j in range(len(sen)):
        if sen[j] == 'kaka':
            res = sen[2]
print("kaka come from "+res)



#3 - Which class Chompey study?
res = ''
for i in range(len(students)):
    sen = students[i]
    for j in range(len(sen)):
        if sen[j] == 'chompey':
            res = sen[1]
print("chompey study in class "+res)



#4 - Replace Chompa province to Prey Veng
res = ''
for i in range(len(students)):
    sen = students[i]
    for j in range(len(sen)):
        if sen[j] == 'chompa':
            sen[2] = 'Prey Veng'
print("chompa come form "+ sen[2])