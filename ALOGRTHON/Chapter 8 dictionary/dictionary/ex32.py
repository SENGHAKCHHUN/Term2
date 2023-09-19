# Ex1 - Object
#Question - Add items to object with difference price
    # name : banana , price : 2
    # name : coconut , price : 4
    # name : mango , price : 3
# array = []
# object1 = {}
# object2 = {}
# object3 = {}
# object1['name'] = 'banana'
# object1['price'] = 2
# array.append(object1)
# object2['name'] = 'coconut'
# object2['price'] = 4
# array.append(object2)
# object3['name'] = 'mango'
# object3['price'] = 3
# array.append(object3)
# print(array)





# -----------------------------------
# Ex2 - Dictionary
fruit_stock = {'banan': 3, 'coconut': 30, 'mango': 21}
#1 - Add new fruit: Orange with amount of 100
# fruit_stock['orange'] = 100
# print(fruit_stock)



#2 - Find average all fruits
# sum = 0
# for key in fruit_stock:
#     sum += fruit_stock[key]
# sum = int(sum / len(fruit_stock))
# print(sum)



#3 - Find total fruit in stock
# print(len(fruit_stock))



#4 - Now change fruit_stock to be input that you can input differneces fruit
# fruit = input()
# fruit_stock[fruit] = 3
# print(fruit_stock)

# fruit_stock = {}
# for i in range(3):
#   fruit = input('enter mk jam')
#   quality = int(input('enter price'))
#   fruit_stock[fruit] = quality
# print(fruit_stock)


# ----------------------------------

# Ex3 - Dictionary or object
fruit_stock = [
  {'name': 'banana', 'quality': 30},
  {'name': 'coconut', 'quality': 10},
  {'name': 'mango', 'quality': 20},
  {'name': 'orange', 'quality': 42},
  {'name': 'apple', 'quality': 25},
]
#1 - Update orange quality to 100
# for key in fruit_stock:
#     if key['name'] == 'orange':
#         key['quality'] = 100
# print(fruit_stock)



#2 - Count the quality of fruit in stock
# sum = 0
# for key in fruit_stock:
#     sum += key['quality']
# print(sum)



#3 - Which fruit have less in stock
# lessN = fruit_stock[0]['quality'] 
# for i in range(len(fruit_stock)):
#     if fruit_stock[i]['quality'] < lessN:
#         lessN = fruit_stock[i]['quality']
# print(lessN)



#4 - Which fruit has the most in stock
# mostN = fruit_stock[0]['quality'] 
# for i in range(len(fruit_stock)):
#     if fruit_stock[i]['quality'] > mostN:
#         mostN = fruit_stock[i]['quality']
# print(mostN)






# ---------------------------------
# Ex4 - Dictionary or object
# fruit_stock = [
#   {'name': 'banana', 'quality': 1},
#   {'name': 'coconut', 'quality': 8},
#   {'name': 'mango', 'quality': 10},
#   {'name': 'orange', 'quality': 0},
#   {'name': 'apple', 'quality': 5},
# ]

#1 - Display fruit that has in stock
# for key in fruit_stock:
#     print(key['name'])


#2 - Display fruit that has more than 5 in stock
# for key in fruit_stock:
#     if key['quality'] > 5:
#         print(key['name'])



#3 - Increase quality of fruit that has less than 10 in stock to 20
# for key in fruit_stock:
#     if key['quality'] < 10:
#         key['quality'] = 20
# print(fruit_stock)