# Ex8 - Dictinary
listFruit = [
  {'name': 'banana', 'price': 10, 'location': 'cambodia'},
  {'name': 'coconu', 'price': 30, 'location': 'Thailand'},
  {'name': 'Jackfruit', 'price': 90, 'location': 'India'},
  {'name': 'orange', 'price': 20, 'location': 'Singapore'},
  {'name': 'orange', 'price': 8, 'location': 'USA'},
]
#1 - Find average of fruit price
# sum = 0
# for i in range(len(listFruit)):
#     sum += listFruit[i]['price']
# print(sum)


#2 - How many fruit type in list
def countFruit(value,array):
    isRun = True
    for j in range(len(array)):
        if array[j] == value:
            isRun = False
    return isRun
listFruit = [
  {'name': 'banana', 'price': 10, 'location': 'cambodia'},
  {'name': 'coconu', 'price': 30, 'location': 'Thailand'},
  {'name': 'Jackfruit', 'price': 90, 'location': 'India'},
  {'name': 'orange', 'price': 20, 'location': 'Singapore'},
  {'name': 'orange', 'price': 8, 'location': 'USA'},
]
newarr = []
count = 0
for i in range(len(listFruit)):
    name = listFruit[i]['name']
    if countFruit(name,newarr):
        newarr.append(name)
        count+=1
print(count)



#3 - Which country has highest price of fruit
# hightest = listFruit[0]['price']
# for i in range(len(listFruit)):
#     if listFruit[i]['price'] > hightest:
#         hightest = listFruit[i]['price']
# print(hightest)


#4 - Which fruti has price lower than 30$
# newarr = []
# for i in range(len(listFruit)):
#     index = 0
#     if listFruit[i]['price'] < 30:
#         newarr.append(listFruit[i]['name'])   
# print(newarr)

# ['banan','orange']


#5 - Which fruit name from Cambodia?
# name = ''
# for i in range(len(listFruit)):
#     if listFruit[i]['location'] == 'cambodia':
#        name = listFruit[i]['name']
# print(name)