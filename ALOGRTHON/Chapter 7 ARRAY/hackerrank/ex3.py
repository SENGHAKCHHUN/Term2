def splitBySpace(text):
    word = ''
    array =[]
    for i in range(len(text)):
        if text[i] == " ":
            array.append(word)
            word = ''
        else:
            word += text[i]
    array.append(word)
    return array
text = input()
print(splitBySpace(text))