# Ex6:
# Count number in list 
# Test case 1:

# Enter array: [1,2,4,10,9]
# Enter number: 10
# ouput
# number 10 is 1

# Test case 2:

# Enter array: [5,4,5, 5, 5, 10,3]
# Enter number: 5
# ouput: 
# number 5 is 4

# Test case 3:

# Enter array: [5,4,10,3]
# Enter numbe 8
# ouput
# number 8 is 0


def countValueinItem(array,value):
    count = 0
    for i in range(len(array)):
        if array[i] == value:
            count+=1
    return count
arr = eval(input("Enter array"))
number = int(input("Enter Number"))
print("number " + str(number) + " is " + str(countValueinItem(arr,number)))