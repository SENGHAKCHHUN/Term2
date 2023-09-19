def comparisonNumber(n1,n2):
    if n1>n2:
        res = str(n1) +" is greater than "+ str(n2)
    else:
        res = str(n1) +" is less than " + str(n2)
    return res
print(comparisonNumber(3,1))
print(comparisonNumber(3,4))
print(comparisonNumber(10,9))