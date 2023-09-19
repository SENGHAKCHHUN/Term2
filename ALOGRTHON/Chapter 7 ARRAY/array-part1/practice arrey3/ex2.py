# def numberOfCompare(array):
#     count = 0
#     if len(array) != 0:  
#         compare = int(array[0])
#         for i in range(len(array)):
#             if compare < int(array[i]):
#                 count +=1
#                 compare = array[i]
#             else:
#                 compare = array[i]
#     return count
# num = eval(input())
# print(numberOfCompare(num))

def find(array):
    res =""
    for i in range(len(array)):
        if array[i] != '7':
            res += array[i]
    return res
array = eval(input())
print(find(array))
