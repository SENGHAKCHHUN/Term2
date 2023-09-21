def keepDoubleLetter(word):
    isFound = False
    for i in range(len(word)):
        if word[i].upper() == 'E' and i != len(word) - 1:
            if word[i + 1].upper() == 'E':
                isFound = True
    return isFound
array = eval(input("enter array"))
newArray = []
for j in range(len(array)):
    if keepDoubleLetter(array[j]):
        newArray.append(array[j])
print(newArray)