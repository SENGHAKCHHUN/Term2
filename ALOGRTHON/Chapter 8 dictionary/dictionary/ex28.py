# Ex6 - object
input1: ['banana','coconut','mango']
input2: [0,1]
[
  {0:'b',1:'a', 2:'n', 3: 'a', 4: 'n',5:'a'},
  {0:'m',1:'a', 2:'n', 3: 'g', 4: 'o'},
]

def makeResult(array,value):
    res = array[value]
    obj = {}
    for i in range(len(res)):
        obj[i] = res[i]
    return obj
input1 = eval(input("enter array "))
input2 = eval(input("enter input 2"))
list = []
for i in range(len(input2)):
    list.append(makeResult(input1,input2[i]))
print(list)

