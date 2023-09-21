array1 = eval(input("enter array1"))
array2 = eval(input("enter array2"))
id = None
count = 0
for i in range(len(array1)):
    if array1[i]['subject'] == 'algorithm':
        count +=1
        id = array1[i]['teacher-id']
        for j in range(len(array2)):
            if array2[j]['teacher-id'] == id:
                print(array2[j]['last-name'],array2[j]['first-name'])
if count == 0:
    print("No teacher in algorithm subject")