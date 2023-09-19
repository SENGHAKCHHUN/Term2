# Ex5 - Array
#Reverse text by index
# input1: ['banana','coconut','mango']
# input2: [0, 2]
# output:
# ['ananab','coconut','ognam']
def reverseWord(array,value):
    res = array[value]
    word = ''
    for i in range(len(res)):
        word += res[-1-i]
    return word
array = eval(input("enter "))
find = eval(input("enter find "))
for i in range(len(find)):
    res = reverseWord(array,find[i])
    array[find[i]] = res
print(array)
