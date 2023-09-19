number = input()
isSmall = int(number[0])
for i in range(len(number)):
    if int(number[i]) < int(isSmall):
        isSmall = number[i]
print(isSmall)