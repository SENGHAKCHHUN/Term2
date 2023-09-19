def isEqual(list1,list2):
    if len(list1) == 0 and len(list2) == 0:
        return "Equal"
    elif len(list1) == len(list2):
        res = ""
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                res = "EQUAL"
            else:
                return "NOT EQUAL"
        return res
    return "NOT EQUAL"
list1 = eval(input())
list2 = eval(input())
print(isEqual(list1,list2))    