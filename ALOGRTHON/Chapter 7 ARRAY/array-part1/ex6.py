# def replaceNumber(number):
#     if len(number)!=0:
#         new_list = []
#         letter = 'x'
#         for item in number:
#             if letter in item:
#                 print(letter)
#                 new_list.append(item)
#         return new_list
#     return []
# n = eval(input())
# print(replaceNumber(n))



# ch = ['eretail', 'retail', 'fax', 'xerox' ]
# input_letter = "x"
# new_list = []
# for item in ch:
#     if input_letter in item:
#         new_list.append(item)
# print(new_list)


# Enter your code here. Read input from STDIN. Print output to STDOUT
def countCharacter(text):
    countA = 0
    countB = 0
    countC = 0
    countD = 0
    res =""
    for i in range(len(text)):
        if text[i]== 'A' or text[i]=='a':
            countA +=1
        elif text[i] == 'b' or text[i] == 'B':
            countB +=1
        elif text[i] == 'C' or text[i] == 'c':
            countB +=1
        elif text[i] == 'D'or text[i] =='d':
            countB +=1
    res = "a:"+ str(countA)+"\n"+"b:"+ str(countB)+"\n"+"c:"+ str(countC)+"\n"+"d:"+str(countD)
    return res
string = input()
print(countCharacter(string))