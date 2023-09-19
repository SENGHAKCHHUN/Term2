# number = input()
# isSeven = False
# i = -1
# sum = 0
# while i < len(number) and not isSeven:
#     if number[i] !='7':
#         sum += int(number[i])
#         i -= 1
#     else:
#         isSeven = True
#         i -= 1
# print (sum)

number = input()
isStop = False
sum = 0
for i in range(len(number)):
    if number[-1-i] != '7' and not isStop:
        sum += int(number[-1-i])
    else:
        isStop = True
print(sum)


    
