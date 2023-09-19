# array2D = [
#     ['*','0','*'],
#     ['*','*','*'],
#     ['*','*','0']
# ]
# i = 0
# run = True
# while i < len(array2D) and run:
#     j = 0
#     bool = True
#     while j < len(array2D[i]) and bool:
#         sign = array2D[i][0]
#         if array2D[i][j] != sign:
#             bool = False
#         j +=1
#     if bool:
#         print("win")
#         run = False
#     i +=1
# if not bool:
#     print("lost")


    
# a = { "cambodia": 17,
#       "thailand" : 30,
#       "france" : 45 }

# print(a["thailand"] )

# studentsAge = { }
# studentsAge['sokan'] = 25
# studentsAge['hak'] = 80
# studentsAge['khmer'] = 1000
# studentsAge.pop('hak')
# for key in studentsAge:
#     print(studentsAge[key])



studentRecord = [
    {"studentName":"Seyla","class":"wep-a","algorithm":98,"html":90},
    {"studentName":"seyha","class":"wep-b","algorithm":80,"html":90},
    {"studentName":"Villa","class":"wep-a","algorithm":96,"html":92},
    {"studentName":"mengheang","class":"wep-a","algorithm":66,"html":54}
]
# sum = 0
# average = 0
# count = 0
# for key in studentRecord:
#     for value in key:
#         if key[value] == 'wep-a':
#             sum += key['algorithm']
#             count +=1
# average = sum / count
# average = int(average)
# print(average)

# _______or______

# sum = 0
# count = 0
# for key in studentRecord:
#     if key['class'] == 'wep-b':
#         sum += key['algorithm']
#         count +=1
# sum = sum / count
# print(sum)



            
    


