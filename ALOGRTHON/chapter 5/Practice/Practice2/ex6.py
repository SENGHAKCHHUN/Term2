def reverseString(string):
    res = ""
    lastIndex = len(string)-1
    for i in range(len(string)):
        res += string[lastIndex-i]
    return res
text = input()
print(reverseString(text))
