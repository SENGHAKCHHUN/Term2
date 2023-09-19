# Ex3 - Sanok has 100$ in his pocket. Now he would like to buy some items in list
arr = ['banana', 'coconut', 'milk', 'ring', 'watch', 'glass']
# Price of each items:
# - banana : 1$
# - coconut: 2$
# - milk: 3$
# - ring: 80$
# - watch: 10$
# - glass: 35$
# #1 - How many items in list?
print(len(arr))


# #2 - How many items Sanok can be with his money
newArr = []
sum = 0
for i in range(len(arr)):
    if arr[i] == 'banana':
        sum +=1
    elif arr[i] == 'coconut':
        sum += 2
    elif arr[i] == 'milk':
        sum += 3
    elif arr[i] == 'ring':
        sum += 80
    elif arr[i] == 'watch':
        sum += 10
    elif arr[i] == 'glass':
        sum += 35
    if sum < 100:
        newArr.append(arr[i])
print(newArr)


# #3 - How much money Sanok need for buying all items
sum = 0
for i in range(len(arr)):
    if arr[i] == 'banana':
        sum +=1
    elif arr[i] == 'coconut':
        sum += 2
    elif arr[i] == 'milk':
        sum += 3
    elif arr[i] == 'ring':
        sum += 80
    elif arr[i] == 'watch':
        sum += 10
    elif arr[i] == 'glass':
        sum += 35
print(sum)