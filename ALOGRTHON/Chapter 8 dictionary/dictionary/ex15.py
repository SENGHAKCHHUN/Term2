# Ex1 - Create new object
# Object container: id, name, quality, price
# number of object : 3
# > {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 100}
# > {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 150}
# > {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 70}
# output:
#   [
#     {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 100},
#     {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 150},
#     {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 70}
#   ]

# newarr = []
# number = int(input())
# for i in range(number):
#     obj = {}
#     obj['id'] = int(input("id "))
#     obj['name'] = input("name ")
#     obj['quality'] = int(input('quality'))
#     obj['price'] = int(input("price "))
#     newarr.append(obj)
# print(newarr)

# ---------------------------


# Ex2 - Dictionary or object
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000}
]
#1 - How many fruit in stock
# print(len(fruit_stock))


#2 - if 1 mango = 2000៛ how much we can get money after sell all mango
# for key in fruit_stock:
#     if key['name'] == 'Mango':
#         res = key['quality'] * 2000
# print(res)


#3 - Following price how much money we can get after sell all fruit from stock
# sum = 0
# res = 0
# for key in fruit_stock:
#     res = key['quality'] * key['price']
#     sum += res
# print(sum)
# ------------------