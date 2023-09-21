array = eval(input("enter array"))
count = 0
newArray = []
for i in range(len(array)):
    if array[i]['subject'] == 'Algorithm':
        if array[i]['score'] < 50:
            count +=1
            newArray.append(array[i]['name'])
obj = {}
obj['number'] = count
obj['stuents'] = newArray
print(obj)