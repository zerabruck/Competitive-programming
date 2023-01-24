input()
first_arr = list(map(int,input().split()))
second_arr = list(map(int,input().split()))

first = 0

second = 0
merged_arr = []

while(True):
    if first == len(first_arr):
        for i in range(second,len(second_arr)):
            merged_arr.append(second_arr[i])

        break
    elif second == len(second_arr):
        for i in range(first,len(first_arr)):
            merged_arr.append(first_arr[i])
        break

    elif first_arr[first] >= second_arr[second]:
        merged_arr.append(second_arr[second])
        second += 1

    else:
        merged_arr.append(first_arr[first])
        first += 1


# print(' '.join([str(i) for i in merged_arr]))

print(*merged_arr)