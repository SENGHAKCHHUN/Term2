# Ex3 - Array append() function

array = []

#1 - add value from 1 to 10 in empty array
sum = 0
for i in range(10):
    sum +=1
    array.append(sum)
print(array)



#2 - add only even number to empty array from 1 to 20
sum = 0
for i in range(20):
    sum +=1
    if sum % 2 == 0:
        array.append(sum)
print(array)



#3 - add value to empty array from 10 to 1
sum = 0
for i in range(10):
    sum = 10 - i
    array.append(sum)
print(array)




#4 - If input as a text example "hi" add each word to empty array => ["h","i"]
name = (input())
for i in range(len(name)):
    array.append(name[i])
print(array)