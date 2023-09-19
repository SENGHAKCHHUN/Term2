arr = eval(input())
list = []
for i in range(len(arr)):
    if arr[i] == 0:
        list.append(arr[i])
        list.append(88)
    elif arr[i] == 1:
        list.append(arr[i])
        list.append(99)
    else:
        list.append(arr[i])
print(list)


arr = eval(input())
for i in range(len(arr)):
    if arr[i] == 0:
        arr.insert(i+1, 88)
    elif arr[i] == 1:
        arr.insert(i+1, 99)
print(arr)