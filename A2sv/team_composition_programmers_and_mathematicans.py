loop = int(input())

for i in range(loop):
    prog,mth = map(int,input().split())
    made_team = 0

    def checker(mid , prog , mth):
        if prog < mid and mth < mid:
            return False
        prog -= mid
        mth -= mid

        summed = prog + mth
        if summed < mid * 2:
            return False
        return True

        
    
    high = min(prog , mth)
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if checker(mid , prog , mth):
            made_team = max(made_team , mid)
            low = mid + 1

        else:
            high = mid - 1 

    print(made_team)
