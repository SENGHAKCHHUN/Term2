
array = eval(input())
i = 0
store = 0
isRun = False
while i < len(array) and not isRun:
    if array[i] != 7:
        store = -1
    else:
        stroe = i
        isRun = True
    i +=1
print(store)