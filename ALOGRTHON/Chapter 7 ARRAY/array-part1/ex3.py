def getIndexOfNumberFive(array):
    if len(array)!=0:
        res = 0
        i=0
        while i < (len(array)):
            if int(array[i]) == 5:
                res = i
                return res
            else:
                res = "None"
            i+=1
        return res
    return None
array = eval(input())
print(getIndexOfNumberFive(array))
