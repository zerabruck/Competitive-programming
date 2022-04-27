from itertools import count
from random import randint


arr = [7,3,2,6,4,1,5,]

result=[]
def checker(arrays):
    temp=arrays[0]
    for i in arrays:
        if(temp>i):
            return False
        temp=i
    return True


def bigger(arrays):
    bigger=arrays[0]
    for i in arrays:
        if(i>bigger):
            bigger=i
    return bigger
  


biggest=bigger(arr)
counter=0
index=0
while(True):
    
    
    if(checker(arr)==True):
        break
    
    for i in range(len(arr)):
        if(biggest==arr[i]):
            index=i       
            break
    # ------------------------------------
   
    


# -------------------------------------------
    
    cutting=arr[0:index+1]
    
    
    result.append(index+1)


    for i in range(len(cutting)):
        arr.pop(0)
        
    for i in cutting:
        arr.insert(0,i)
    # --------------------------------------------------


    cutting=arr[0:len(arr)-counter]
    result.append(len(arr)-counter)
    for i in range(len(cutting)):
        arr.pop(0)
        
    for i in cutting:
        arr.insert(0,i)
    
    counter+=1
    biggest-=1




print(arr)