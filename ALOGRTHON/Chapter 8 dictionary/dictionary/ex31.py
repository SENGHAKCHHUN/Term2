# Ex9 - Array
#Replace character by something
# input1: ['banana','coconut','mango']
# input2: ['a', '*']
# output:
# ['b*n*n*','coconut','m*ngo']


def repleace(word,value):
    res = ''
    for j in range(len(word)):
        if word[j] == value[0]:
            res += value[1]
        else:
            res += word[j]
    return res
text = eval(input('enter '))
find = eval(input("enter "))
for i in range(len(text)):
    text[i] = repleace(text[i],find)
print(text)
