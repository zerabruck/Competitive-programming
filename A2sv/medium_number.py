loop = int(input())

for i in range(loop):
    number = list(map(int,input().split()))
    number.sort()
    print(number[1])