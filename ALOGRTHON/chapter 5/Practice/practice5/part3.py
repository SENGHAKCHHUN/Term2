# ________part1________
# def countCharacter(word,char):
#     count = 0
#     for i in range(len(word)):
#         if word[i] == char:
#             count +=1
#     return count
# word = input("Enter a word")
# char = input("Enter character to count: ")
# print(countCharacter(word,char))

# __________part2____________
def countCharacter(word,char):
    count = 0
    for i in range(len(word)):
        if word[i] == char:
            count +=1
    return count
isGoon = True
while isGoon:
    word = input("Enter a word:")
    char = input("Enter character to count:")
    print(countCharacter(word,char))
    Continue = input("Do you want to continue(Y/N)?")
    if Continue.upper() !='Y':
        isGoon = False