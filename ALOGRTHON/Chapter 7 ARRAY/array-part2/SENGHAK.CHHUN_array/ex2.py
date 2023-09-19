# Ex2 - Basic array

array = [1, 4, 5, 2, 9, 1, 6, 3, 2]

#1 - Find average of value in array
n = len(array)
sum = 0
average = 0
for i in range(n):
    sum += array[i]
average = sum / n
print(average)



#2 - Find max / min value in array
max = array[0]
min = array[0]
for i in range(len(array)):
    if max < array[i]:
        max = array[i]
    elif min > array[i]:
        min = array[i]
print("Max " + str(max) +"\n" + "Min " + str(min))        



#3 - If odd value add 1 and if even value minus 1
odd = 1
even = 1
for i in range(len(array)):
    if array[i] % 2 != 0:
        array[i]+= 1
    else:
        array[i] -= 1
print(array)



#4 - How many number < 5 in array
count = 0
for i in range(len(array)):
    if array[i] < 5:
        count +=1
print(count)



#5 - Square value of array
square = 1
for i in range(len(array)):
    array[i] = array[i] * array[i]
print(array)