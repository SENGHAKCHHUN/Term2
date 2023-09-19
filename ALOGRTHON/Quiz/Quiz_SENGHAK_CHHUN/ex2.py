def containUpperCase(word):
    isFalse = False
    i = 0
    while i < len(word) and not isFalse:
        if word[i].isupper():
            isFalse = True
            res = "VALID"
        else:
            res = "INVALID"
        i +=1
    return res
word = input()
print(containUpperCase(word))
