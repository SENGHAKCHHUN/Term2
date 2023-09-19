array = eval(input())
arr =[]
for i in range(len(array)):
    if array[i] == 'X'and i < len(array)-1:
        arr.append(array[i+1])
    elif array[i-1] == 'X' and i > 0:
        arr.append(array[i-1])
    else:
        arr.append(array[i])
print(arr)