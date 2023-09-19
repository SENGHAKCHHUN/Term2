# n1 = input("n1")
# n2 = input("n2")
# String = n1 + ';' + n2
# result = ""
# i = 0
# isStop = False
# while i < len(String) and not isStop:
#     if String [2] == ';':
#         if len(n1) == 2 and len(n2) == 2 and String[i].isnumeric():
#             sum  = int(n1) + int(n2)
#             print(sum)
#             isStop = True
#         else:
#             print("WORNG")
#         isStop = True
#     else:
#         print("WORNG")
#         isStop = True
#     i +=1




number = input()
result1 = ""
result2 = ""
isSeven = False
for i in range(len(number)):
    if number[i] != ";" and not isSeven:
        result1 += number[i]
    elif number[i] == ";":
        isSeven = True
    else:
        result2 +=number[i]
if len(result1) == len(result2):
    sum = int(result1 ) + int(result2)
    print(sum)
else:
    print(-1)
    