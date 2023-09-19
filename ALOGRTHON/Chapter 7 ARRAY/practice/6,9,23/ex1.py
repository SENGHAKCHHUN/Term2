def makeArray2D(row,col):
    newarr = []
    for i in range(row):
        newarr.append([])
        for j in range(col):
            newarr[i].append('0')
    return newarr
row = int(input('Enter row '))
col = int(input('Enter column '))
print(makeArray2D(row,col))

