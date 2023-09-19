number = eval(input())
arr = []
sum = 0
i = 0
isRun = False
while i <len(number) and not isRun:
    if sum < 200:
        sum += number[i]
        arr.append(number[i])
    elif sum >= 200:
        isRun = True
    i +=1
if sum >= 200:
    print(arr)
else:
    print("[]")