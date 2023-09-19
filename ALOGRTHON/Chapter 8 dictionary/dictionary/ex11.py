# Ex1 - String
text = "aba is the bank in cambodia"
#1 - add text to array
# i = 0
# word = ''
# newlist = []
# while i < len(text):
#     if text[i] == ' ':
#         newlist.append(word)
#         word = ''
#     else:
#         word += text[i]
#     i +=1
# newlist.append(word)
# print(newlist)
        
# ['aba', 'is', 'the', 'bank', 'in', 'cambodia']

#2 - Find first index of "B"
# index = None
# bool = True
# i = 0
# while i < len(text) and bool:
#     if text[i].upper() == 'B':
#         index = i
#         bool = False
#     i +=1
# print(index)


#3 - Convert text to capitalize
# "Aba Is The Bank In Cambodia"
# text = "aba is the bank in cambodia"
# res = ''
# text[0].upper()
# for i in range(len(text)):
#     if text[i] == ' ':
#         bool = True
#         res += text[i]
#     elif bool:
#         res += text[i].upper()
#         bool = False
#     else:
#         res += text[i]
# print(res)

#4 - Reverse text
# text = "aba is the bank in cambodia"
# res = ''
# loop = 0
# result = ''
# for i in range(len(text)):
#     if text[i] == ' ' or i == len(text)-1:
#         for i in range(len(res)):
#             result += res[-1-i]
#         result += ' '
#         res = ''
#     else:
#         res += text[i]
# print(result)


        
# "aba si eht knab ni aidobmac"