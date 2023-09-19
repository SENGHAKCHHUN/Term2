# Ex2 - Array
arr = [1010, 55, 993, 2]
#1 - How many degit of each number
# for i in range(len(arr)):
#     string = str(arr[i])
#     res = len(string)
#     arr[i] = res
# print(arr)


# [4, 2, 3, 1]
#2 - Reverse array
# list = []
# for i in range(len(arr)):
#     list.append(arr[-1-i])
# print(list)


#3 - Sum only number > 2 degit
sum = 0
for i in range(len(arr)):
    string = str(arr[i])
    n = len(string)
    if n > 2:
        sum += arr[i]
print(sum)