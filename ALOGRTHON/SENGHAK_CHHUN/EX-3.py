def reverseText(text):
    res = ''
    for j in range(len(text)):
        res += text[-1-j]
    return res
array = eval(input("Enter array"))
newArray = []
for i in range(len(array)):
    newArray.append(reverseText(array[-1-i]))
print(newArray)