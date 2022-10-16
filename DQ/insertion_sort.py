arr=[9,10,3,6,1,-1]

for i in range(1,len(arr)):
    for j in range(i-1,-1,-1):
        if(arr[i]>=arr[j]):
            
            print(arr[i])
            print(arr[j])
            
            value=arr.pop(i)
            print(arr)
            arr.insert(j+1,value)
            print(arr)
            print(
                '-------------'
            )
            break
        if(j==0):
            arr.insert(0,arr.pop(i))
            print('hey')


print(arr)