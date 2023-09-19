# Ex4 - Array pop() function

array = [1, 2, 5, 7, 9, 7, 4, 8]

# # 1 - Remove number 3 from list
arr = []
for i in range(len(array)):
    if array[i] != 3:
        arr.append(array[i])
print(arr)


# 2 - Remove first 7 from list
i = 0
isFalse = False
while i < len(array) and not isFalse:
    if array[i] == 7:
        array.pop(i)
        isFalse = True
    i +=1
print(array)


#3 - Remove only odd number from list
arr = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        arr.append(array[i])
print(arr)


#4 - Remove only value < 5 from list
arr = []
for i in range(len(array)):
    if array[i] > 5:
        arr.append(array[i])
print(arr)
