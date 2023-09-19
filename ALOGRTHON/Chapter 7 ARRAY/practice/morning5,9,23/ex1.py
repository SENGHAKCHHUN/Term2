# Ex1 - String
# text = "38347"


#1 - Sum all number in string (function)
def sumNumber(text):
    sum = 0
    for i in range(len(text)):
        sum += int(text[i])
    return sum
text = "38347"
print('sum all number in string is '+ str(sumNumber(text)))


#2 - Find average of number in string (function)
def averageNumber(text):
    average = 0
    sum = 0
    for i in range(len(text)):
        sum += int(text[i])
    average = sum / len(text)
    average = int(average)
    return average
text = "38347"
print('average of number in string is '+ str(averageNumber(text)))


#3 - Reverse the string (function)
def reversedString(text):
    res = ''
    for i in range(len(text)):
        res += text[-1-i]
    return res
text = "38347"
print('Reverse the string is ' + reversedString(text))