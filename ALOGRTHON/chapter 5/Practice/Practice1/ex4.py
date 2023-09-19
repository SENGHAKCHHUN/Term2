def sumFromTo(n1,n2):
    sum = 0
    if n1 < n2:
        for i in range(n1,n2+1):
            sum += i
        return sum
    else:
        return 0
n1 = int(input("start value"))
n2 = int(input("end value"))
print("The sum number between", n1 ,"and" ,n2 ,"is :", sumFromTo(n1,n2))


# def sum(n1,n2):
#     return n1+n2
# def sumFromTo(start,end):
#     total = 0
#     while start <= end:
#         total += start
#         start = start+1
#     return total
# num1 = int(input("enter start"))
# num2 = int(input("enter end")) 
# print("The sum number between",num1 ," and ",num2 ,"is: ",sumFromTo(num1,num2))


