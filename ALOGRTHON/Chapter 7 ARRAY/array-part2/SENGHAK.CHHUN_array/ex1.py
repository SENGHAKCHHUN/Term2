# Ex1 - Basic array

array = [1, 4, 5, 2, 9, 1, 6, 3, 2]

#1 - How many value in array
print(len(array))


#2 - Sum all value in array
sum = 0
for i in range(len(array)):
    sum += array[i]
print(sum)



#3 - Count even / odd number in array
even= 0
odd = 0
for i in range(len(array)):
    if array[i] % 2 == 0:
        even+=1
    else:
        odd +=1
print("even " + str(even) +"\n"+ "odd " + str(odd))



#4 - Find first index of 2
find = 0
i = 0
bool = False
while i < len(array) and not bool:
    if array[i] == 2:
        find = i
        bool = True
    i +=1
print(find)




#5 - Replace number 1 by 88 and 2 by 99
for i in range(len(array)):
    if array[i] == 1:
        array[i] = 88
    elif array[i] == 2:
        array[i] = 99
print(array)



#6 - If value is 1 add 3 more and if value greater than 2 minus 1
add = 3
minus =1
for i in range(len(array)):
    if array[i] == 1:
        array[i] += add
    elif array[i] > 2:
        array[i] -= minus
print(array)

