# Ex7 - Array (while only)
# arr = [1024, 1010, 2024, 123454]
#1 - How many degit each item
# i = 0
# newList = []
# number = ''
# while i < len(arr):
#     number = str(arr[i])
#     n = len(number)
#     newList.append(n)
#     i +=1
# print(newList)
# [4, 4, 4, 6]


#2 - Sum each number in each value together (1 + 0 + 2 + 4)
# newlist = []
# number = ''
# i = 0
# sum = 0
# while i < len(arr):
#     number = str(arr[i])
#     j = 0
#     while j < len(number):
#         sum += int(number[j])
#         j +=1
#     newlist.append(sum)
#     sum = 0
#     i +=1
# print(newlist)



#3 - Sum only last degit number on each item (4 + 0 + 4 + 4)
i = 0
sum =0
n = ''
num = 0
arr = [1024, 1010, 2024, 123454]
while i < len(arr):
    n = str(arr[i])
    num = n[len(n)-1]
    sum += int(num)
    i +=1
print(sum)

# sum = 12