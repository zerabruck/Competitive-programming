n_k = list(map(int,input().split()))
k = n_k[1]

n = n_k[0]

nums = list(map(int,input().split()))
nums.sort()
if n == k :
    print(nums[k - 1])
elif k == 0:
    if nums[0] != 1:
        print(1)
    else:
        print(-1)
elif n > k and nums[k] != nums[k - 1]:
    print(nums[k - 1])

else:
    print(-1)
