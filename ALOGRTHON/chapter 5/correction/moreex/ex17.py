group = input()
groupLetter = ""
groupNumber = ""
for i in range(len(group)):
    if group[i].isnumeric():
        groupNumber += group[i]
    else:
        groupLetter += group[i]
print(str(groupNumber) + str(groupLetter))