arr = eval(input())
sum = 0
average = 0
if len(arr) > 0:
    for i in range(len(arr)):
        sum += arr[i]
    average = sum / len(arr)
    if average > 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")