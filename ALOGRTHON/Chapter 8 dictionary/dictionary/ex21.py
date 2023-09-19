# Ex8 - Dictionary or object
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quatity': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quatity': 0, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quatity': 23, 'price': 2000},
  {'id': 4, 'name': 'Orange', 'quatity': 0, 'price': 5000},
  {'id': 5, 'name': 'Apple', 'quatity': 5, 'price': 3000},
  {'id': 6, 'name': 'Jackfruit', 'quatity': 13, 'price': 6000},
]
#1 - How many fruit have price > 3000
# numberOfFruit = 0
# names = []
# obj = {}
# for key in fruit_stock:
#     if key['price'] > 3000:
#         numberOfFruit += 1
#         names.append(key['name'])
# obj['numberoffruit'] = numberOfFruit
# obj['names'] = names
# print(obj)

# {
#   'numberOfruit': 3,
#   'names': ['Coconut','Orange', 'Jackfruit']
# }



# --------------------
#2 - How many fruit have price < 5000
# list = []
# for i in range(len(fruit_stock)):
#   if fruit_stock[i]['price'] < 5000:
#     res = fruit_stock[i]['name']
#     obj = {}
#     obj['name'] = res
#     list.append(obj)
# print(list)

# [
#   {'name': 'Coconut'},
#   {'name': 'Banana'},
#   {'name': 'Mango'},
#   {'name': 'Apple'}
# ]
# -------------------
#3 - Which fruit doens't have in stock
# [
#   {'name': 'Banana', 'quatity': 0},
#   {'name': 'Orange', 'quatity': 0}
# ]
list = []
for i in range(len(fruit_stock)):
  if fruit_stock[i]['quatity'] == 0:
    res = fruit_stock[i]['name']
    obj = {}
    obj['name'] = res
    obj['quatity'] = 0
    list.append(obj)
print(list)
