from random import randint


arr = [3,2,4,1]

result=[]
def checker(arrays):
    temp=arrays[0]
    for i in arrays:
        if(temp>i):
            return False
        temp=i
    return True

while(True):
    if(checker(arr)==True):
        break
    value=randint(1,len(arr))
    cutting=arr[0:value]
    result.append(value)

    for i in range(len(cutting)):
        arr.pop(0)
        
    for i in cutting:
        arr.insert(0,i)

print(result)