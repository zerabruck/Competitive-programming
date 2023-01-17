loop = int(input())

for i in range(loop):
    first_side = list(map(int,input().split()))
    second_side = list(map(int,input().split()))

    max_first = max(first_side)
    max_second = max(second_side)
    min_first = min (first_side)
    min_second = min(second_side)
    summ = min_first + min_second

    if max_first == max_second and max_first == summ:
        print('YES')

    else:
        print('NO')



   

