# Ex5 - Array 2D
# We have 2 input row and column create array 2D with value '0'
# Case:
# row: 2
# col: 2
# output:
# [['0','0'],['0','0']
row = int(input("row "))
col = int(input("col "))
newarr = []
for i in range(row):
    newarr.append([])
    for j in range(col):
        newarr[i].append('leak')
print(newarr)
