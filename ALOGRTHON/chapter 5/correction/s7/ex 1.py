# number = input()
# isTrue = False
# i = 0
# sum = 0
# while number[i] != '7' and not isTrue:
#     sum += int(number[i])
#     i +=1
# else:
#     isTrue = True
#     print(sum)


number = input()
sum = 0
isStop = False
for i in range(len(number)):
    if number[i] != '7' and not isStop:
        sum += int(number[i])
    else:
        isStop = True
print(sum)
