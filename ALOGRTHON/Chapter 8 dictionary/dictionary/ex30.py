# Ex8 - Object
#Reverse Object
# input: {1: 'banana', 2: 'mango', 3: 'coconut'}
# output: {1: 'ananab', 2: 'ognam', 3: 'tunococ'}


def reverseWord(word):
    res = ''
    for i in range(len(word)):
        res += word[-1-i]
    return res
text = eval(input())
for key in text:
    text[key] = reverseWord(text[key])
print(text)



     

    

