# Ex3 - Array
#Find index
input1: [3, 3, 4, 5, 6, 6]
input2: [3, 4, 6]
ouput: {3: [0, 1], 4: 2, 6:[4, 5]}

def findIndex(array,value):
    index = ''
    list = []
    count = 0
    for i in range(len(array)):
        if array[i] == value:
            index += str(i)
            count +=1
    if count > 1:
        for i in range(count):
            list.append(int(index[i]))
        return list
    else:
        index = int(index)
        return index
arr1 = eval(input("enterarray "))
arr2 = eval(input("enter "))
obj = {}
for a in range(len(arr2)):
    obj[arr2[a]] = findIndex(arr1,arr2[a])
print(obj)
    




