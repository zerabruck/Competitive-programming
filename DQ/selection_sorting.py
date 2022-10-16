arr=[2,5,6,3,1]

for i in range(len(arr)):
    min=i
    for j in range(i,len(arr)):
        if(arr[min]>arr[j]):
            min=j
    arr[i],arr[min]=arr[min],arr[i]

print(arr)
