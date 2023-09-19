arr = eval(input())
number = 0
list = []
for i in range(len(arr)):
    number = arr[i]
    max = number[0]
    for j in range(len(number)):
        if max < number[j]:
            max = number[j]
    list.append(max)
print(list)