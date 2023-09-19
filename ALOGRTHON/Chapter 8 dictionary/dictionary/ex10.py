# Ex9 Array - Dictinary
# arrText = ['banana','orange','coconut','mango']
# arrNumber = [10, 30, 20, 9]
#Q - create array of dictionary following 2 array above
# [
#   {'banana':10},
#   {'orange': 30},
#   {'coconut': 20}
#   {'mango': 9}
# ]
# list = []
# for i in range(len(arrText)):
#     res = {}
#     res[arrText[i]]= arrNumber[i]
#     list.append(res)
# print(list)


arrText = ['leak','hak','pu','pov','chan','maly','mother','dad','yiem','ya']
arrNum = [1,2,3,4,5,6,7,8,9,10]
newlist = []
for i in range(len(arrText)):
    object = {}
    object[arrText[i]] = arrNum[i]
    newlist.append(object)
print(newlist)
