loop = int(input())

for i in range(loop):
    first_side = list(map(int,input().split()))
    second_side = list(map(int,input().split()))
    value=-1
    indexx = []
    for ind,col in enumerate(first_side):
        if col in second_side:
            indexx.append(ind)
            indexx.append(second_side.index(col))
            value = col
            break
    if value != -1:
        first_side.pop(indexx[0])
        second_side.pop(indexx[1])
    summed = first_side[0] + second_side[0]
    if value == -1:
        print("NO")
    elif value != summed:
        print("NO")
    else:
        print("YES")
   

