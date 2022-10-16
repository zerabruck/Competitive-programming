arr=[2,14,7,4,4,20,2,1,8,2,5,9,0,4,2]
maxim=max(arr)
first_arr=[ 0 for i in range(maxim+1)]
print(first_arr)
for i in arr:
    first_arr[i]+=1

print(first_arr)


new_arr=[]

for i in range(len(first_arr)):
    for j in range(first_arr[i]):
        new_arr.append(i)


print(new_arr)

print( 2==4/2)

for i in range(1,len(arr),2):
    print(i)