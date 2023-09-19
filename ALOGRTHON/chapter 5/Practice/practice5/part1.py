# ____________ex1___________
# def multiply(n1,n2):
#     return n1*n2
# print(multiply(2,3))


# _____________ex2____________
def multiply(n1,n2):
    return n1*n2
def multiplyNumber(num1,num2):
    res = 1
    while num1 < num2+1:
        res = multiply(res,num1)
        num1 +=1
    return res
startNumber = int(input("startNumber"))
endNumber = int(input("endNumber"))
print(multiplyNumber(startNumber,endNumber))