arr=[-2,45,0,11,-9]

for i in range(len(arr)):
    for j in range(1,len(arr)):
        if(arr[j]<arr[j-1]):
            arr[j],arr[j-1]=arr[j-1],arr[j]


print(arr)