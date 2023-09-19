# ------------------------------
# Ex2 - Array
# arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]


#1 - Sum all number (function)
def sumNumber(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
print('Sum all number in array '+ str(sumNumber(arr)))


#2 - Reverse array (function)
def reverseArray(array):
    newarr = []
    for tra in range(len(array)):
        newarr.append(array[-1-tra])
    return newarr
arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
print(reverseArray(arr))


#3 - Find index of 3 (function)
def FindIndex(array):
    index = None
    for leak in range(len(array)):
        if array[leak] == 3:
            index = leak
    return index
arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
print("Index of 3 is "+str(FindIndex(arr)))


#4 - Romove 8 number from list (function)
def RemoveEight(array):
    index = 0
    for rean in array:
        if rean == 8:
            index = rean
    arr.remove(index)
    return arr
arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
print(RemoveEight(arr))


#5 - Remove duplicate value (function)
def removeDuplicateValue(value,newarr):
    isTrue = True
    for vor in range(len(newarr)):
        if value == newarr[vor]:
            isTrue = False
    return isTrue
arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
newarr = []
for leak in range(len(arr)):
    if removeDuplicateValue(arr[leak],newarr):
        newarr.append(arr[leak])
print(newarr)


#6 - Replace 10 by 99
arr = [10, 12, 3, 8, 9, 12, 12, 10, 10]
for i in range(len(arr)):
    if arr[i] == 10:
        arr[i] = 99
print(arr)