# Ex1 - String
numberInString = "10 30 4 12"
#1 - How many number in string
# count = 0
# for i in range(len(numberInString)):
#     if numberInString[i].isnumeric():
#         count +=1
# print(count)


#2 - Sum all value seperated by space
# sum = 0
# number = ''
# for i in range(len(numberInString)):
#     if numberInString [i]!= ' ':
#         number += numberInString[i]
#     else:
#         sum += int(number)
#         number = ''
# sum += int(number)
# print(sum)

# or
number = ''
sum = 0
for i in range(len(numberInString)):
    if numberInString[i] == ' ' or i == len(numberInString) - 1:
        if i == len(numberInString)-1:
            number += numberInString[i]
        sum += int(number)
        number = ''
    else:
        number += numberInString[i]
print(sum)

#3 - Find average of number
# sum = 0
# number = ''
# count = 0
# for i in range(len(numberInString)):
#     if numberInString [i]!= ' ':
#         number += numberInString[i]
#     else:
#         sum += int(number)
#         number = ''
#         count +=1
# sum += int(number)
# average = sum / count
# average = int(average)
# print(average)


# ------------
# Ex2 - String
text = "Welcome to Phnom Penh"
#1 - how amny letter in string
# count = 0
# for i in range(len(text)):
#     if text[i] != ' ':
#         count +=1
# print(count)


#2 - Reverse string
# res = ''
# for i in range(len(text)):
#     res += text[-1-i]
# print(res)


#3 - add string to arr : ['welcome', 'to', 'phnom', 'penh']
arr = []
word = ''
for i in range(len(text)):
    if text[i] != ' ':
        word += text[i]
    else:
        arr.append(word)
        word = ''
arr.append(word)
print(arr)