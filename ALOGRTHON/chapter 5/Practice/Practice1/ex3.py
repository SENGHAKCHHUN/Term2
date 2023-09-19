# ______Tip1_____
def sum():
    number = int(input("Number of values"))
    res =  0
    for i in range(number):
        value = int(input("value "+str(i+1) + ":"))
        res += value
    return res
print("The sum is:",sum())

# ______Tip2______
def sum(n1, n2):
    return n1 + n2
numberOfTimes = int(input("Number of times:"))
result = 0
for i in range(numberOfTimes):
    number = int(input("Value " + str(i + 1) + ": "))
    if i == 0:
        prevuisValue = number
    else:
        prevuisValue = sum(prevuisValue, number)
    result = prevuisValue
print(result)