# Ex1 - Array
input1: ['banana','coconut','mango']
input2: ['a','o']
# output:
# {'a': 4, 'o': 3]
def checkValue(input1,value):
    count = 0
    for i in range(len(input1)):
        for k in range(len(input1[i])):
            if input1[i][k] == value:
                count +=1
    return count
list = []
input1 = eval(input("enter list "))
input2 = eval(input("enter list "))
obj = {}
for i in range(len(input2)):
    obj[input2[i]] = (checkValue(input1,input2[i]))
print(obj)
