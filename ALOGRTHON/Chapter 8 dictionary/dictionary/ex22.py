# Ex9 - Array - Object or array dictionary
fruits = [
  {'bmc': ['banana','coconut', 'apple','mango']},
  {'btb': ['orange', 'banana']},
  {'sr': ['jackfruit','coconut', 'banana']}
]
#1 - Which province has fruit the most?s
max = 0
for key in fruits:
  for value in key:
    if max < len(key[value]):
      max = len(key[value])
      name = value
print(name + " is the province has fruit the most is " + str(max))




# newlist = []
# big = len(fruits[0]['bmc'])
# name = 'bmc'
# print(big)
# Name = 'bmc'
# for i in range(len(fruits)):
#   name = input("enter ")
#   n = len(fruits[i][name])
#   if big < n:
#     big = n
#     Name = name
#   print(fruits[i])
# print(Name + " is the province has fruit the mose is " + str(big))








#2 - Which province has coconut
list = []
for key in fruits:
  for value in key:
    for i in range(len(key[value])):
      obj = {}
      if key[value][i] == 'coconut':
        obj['province'] = value
        list.append(obj)
print(list)


# [
#   {'province': 'bmc'},
#   {'province': 'sr'}  
# ]
# for i in range(len(fruits)):
#   name = input("enter")
#   for j in range(fruits[i][name]):
#     print([j][name])
      



#3 - How many banana in fruit list
# {'banana': 3}
count = 0
for key in fruits:
  for value in key:
    for i in range(len(key[value])):
      if key[value][i] == 'banana':
        count +=1
obj = {}
obj['banana'] = count
print(obj)


#4 - add mango to btn province
btn = {}
list = []
list.append('mango')
btn['btn'] = list
fruits.append(btn)
print(fruits) 