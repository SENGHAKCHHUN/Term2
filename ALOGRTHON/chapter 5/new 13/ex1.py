value = input()
n = len(value)
result = ""
isStop = False
for i in range(n):
    if value[0].upper()== value[i].upper() and not isStop :
        result = "Okay"
    else:
        isStop = True
        result = "No"
print(result)
count = 0
isFound = False
if value == "[khmer temple] leak":
    for i in range(len(value)):
        if value[i] != "[" or value[i] != " " and not isFound:
            count += 1
        elif value[i]=="]":
            isFound = True
print(count)
