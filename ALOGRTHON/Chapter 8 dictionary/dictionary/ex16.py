# Ex3 - Dictionary or object
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 0, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000},
  {'id': 4, 'name': 'Orange', 'quality': 0, 'price': 5000},
  {'id': 5, 'name': 'Apple', 'quality': 5, 'price': 3000},
  {'id': 6, 'name': 'Jackfruit', 'quality': 13, 'price': 6000},
]
#1 - How many fruit have in stock
# print(len(fruit_stock))


#2 - How many fruit no more in stock
# count = 0
# for key in fruit_stock:
#     if key['quality'] == 0:
#         count +=1
# print(count)


#3 - Add 10 fruit to stock which fruti doesn't exist
# for key in fruit_stock:
#     if key['quality'] == 0:
#         key['quality'] = 10
# print(fruit_stock)

#4 - Add fruit name to array
# name = {}
# name['name'] = 'pineapple'
# fruit_stock.append(name)
# print(fruit_stock)

#5 - Calculate total of price after add 10 to empty fruit
sum = 0
for key in fruit_stock:
    if key['quality'] == 0:
        key['quality'] = 10
    res = key['quality'] * key['price']
    sum += res
print(sum)