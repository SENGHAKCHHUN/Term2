def removeSpace(word):
    count =0
    for i in range(len(word)):
        if word[i] !=' ':
            count+=1
    return count
text = input()
print(removeSpace(text))
        