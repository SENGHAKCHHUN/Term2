# Ex5:
# Find index of number in list (each value is unique)
# Test case 1:

# Enter array: [1,2,4,10,9]
# Enter number: 10
# ouput
# 10 at position 3


# Test case 2:

# Enter array: [5,4,10,3]
# Enter number: 5
# ouput
# 5 at position 0

# Test case 3:

# Enter array: [5,4,10,3]
# Enter number: 8
# ouput
# 8 not found in list

def findNumber(array,value):
    i =0
    bool = False
    while i < len(array) and not bool:
        if array[i] == value:
            index = i
            bool = True
        else:
            index = str(value) + ' not found in list'
        i +=1
    return index
array = eval(input("enter array"))
number = int(input("enter number"))
print(findNumber(array,number))