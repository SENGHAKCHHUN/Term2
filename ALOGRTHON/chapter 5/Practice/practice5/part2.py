# ___________part1_____________
# def removeCharacter(word, char):
#     res =""
#     for i in range(len(word)):
#         if word[i]!= char:
#             res += word[i]
#     return res
# word = input("word")
# char = input("removeb")
# print(removeCharacter(word,char))

# ____________part2____________

def removeCharacter(word,char):
    res =""
    for i in range(len(word)):
        if word[i]!= char:
            res += word[i]
    return res
nextStep = "Y"
while nextStep == "Y":
    word = input("Enter a Word")
    char = input("Enter a character to remove:")
    print(removeCharacter(word,char))
    nextStep = input("Do you want to continue (Y/N)? ").upper()   
    
        