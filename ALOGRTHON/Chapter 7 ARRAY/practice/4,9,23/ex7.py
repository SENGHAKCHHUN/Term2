# Ex7:
# Count number 10 in list of array 2D
# Test case 1:

# Enter array: [[1, 2, 4, 5], [14, 16, 10, 11], [10, 9, 10, 10]]
# ouput
# number 10 is 4

# Test case 2:
# Enter array: [[1, 2, 4, 5], [14, 16, 8, 11], [8, 9, 8, 8]]
# ouput
# number 10 is 0
def findNumberTen(array):
    count = 0
    for i in range(len(array)):
        if array[i] == 10:
            count +=1
    return count
list = eval(input("Enter "))
total = 0
for i in range(len(list)):
    res = findNumberTen(list[i])
    total += res
print("number 10 is " + str(total))
