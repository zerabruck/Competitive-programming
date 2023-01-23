loop = int(input())

arrays = []

for i in range(loop):
    laptop = list(map(int,input().split()))
    arrays.append(laptop)

arrays.sort(reverse=True)
smallest = arrays[0][1]

for price,quailty in arrays:
    if smallest < quailty:
        print("Happy Alex")
        exit()

    else:
        smallest = min(smallest,quailty)
print("Poor Alex")



        