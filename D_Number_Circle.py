input()

numbers = list(map(int,input().split()))

numbers.sort()

added_val = numbers[-3] + numbers[-2]

if added_val > numbers[-1]:
    print('YES')
    strings = ' '.join([str(i) for i in numbers])
    print(strings)

else:
    print('NO')