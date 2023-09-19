def numberOfUpperCases(string):
    count = 0
    for i in range(len(string)):
        if string[i].isupper():
            count+=1
    return count
word = input()
print("Number of Uppercase "+str(numberOfUpperCases(word)))




# def numberOfUpperCases(string):
#     count = 0
#     i=0
#     while i < len(string):
#         if string[i].isupper():
#             count+=1
#         i+=1
#     return count
# text = input()
# print(numberOfUpperCases(text))
