input()

nums = list(map(int,input().split()))
odds = 0
evens = 0

for i in nums:
    if i % 2 == 0:
        evens += 1

    elif i % 2 != 0:
        odds += 1

if odds != 0 and evens != 0:
    nums.sort()
    print(*nums)

else:
    print(*nums)