input()
first_arr = list(map(int,input().split()))
second_arr = list(map(int,input().split()))
result = []

first_pointer = 0

for num in second_arr:
    while first_pointer != len(first_arr):
        if  num <= first_arr[first_pointer]:
            break

        first_pointer += 1

    result.append(first_pointer)

print(*result)