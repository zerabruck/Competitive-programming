arr = [10,20,30,40,5]

for num in range(len(arr)-1):
    if arr[num] > arr[num + 1]:
        print("yes")
        exit()

print("No")