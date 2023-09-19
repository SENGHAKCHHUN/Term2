array = eval(input())
count = 0
number = array[0]
for i in range(len(array)):
    if number < array[i]:
        count +=1
        number = array[i]
    else:
        number = array[i]
print(count)