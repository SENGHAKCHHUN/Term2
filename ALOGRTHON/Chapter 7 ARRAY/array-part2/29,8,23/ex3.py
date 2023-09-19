# Ex7 - Array (while only)
arr = [1024, 1010, 2024, 123454]
#1 - How many degit each item
i = 0
newArr = []
while i < len(arr):
    number = str(arr[i])
    n = len(number)
    newArr.append(n)
    i += 1
print(newArr)
# [4, 4, 4, 6]



#2 - Sum each number in each value together (1 + 0 + 2 + 4)
newlist = []
i = 0
number = ''
sum = 0
while i < len(arr):
    number = str(arr[i])
    j = 0
    while j < len(number):
        sum += int(number[j])
        j +=1
    newlist.append(sum)
    sum = 0
    i +=1
print(newlist)
[7, 2, 8, 19]




#3 - Sum only last degit number on each item (4 + 0 + 4 + 4)
# sum = 12
index = 0
i = 0
sum = 0
while i < len(arr):
    number = str(arr[i])
    n = number[len(number)-1]
    sum += int(n)
    i += 1
print(sum)
