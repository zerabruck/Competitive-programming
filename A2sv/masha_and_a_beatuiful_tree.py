def merger(left_arr , right_arr , count):
    if left_arr[-1] < right_arr[-1]:
        left_arr.extend(right_arr)
        return left_arr
    else:
        count[0] += 1
        right_arr.extend(left_arr)
        return right_arr

def merge_sort(left , right , arr , count):
    if left == right:
        return [arr[left]]
    
    mid = (left + right) // 2
    left_arr = merge_sort(left , mid , arr , count)
    right_arr = merge_sort(mid + 1 , right , arr , count)
    return merger(left_arr , right_arr , count)
# accepting input

cases = int(input())

for i in range(cases):
    input()
    arr = list(map(int,input().split()))
    set_arr = set(arr)
    if len(arr) != len(set_arr):
        print(-1)

    else:
        count = [0]
        sorted_arr = merge_sort(0 , len(arr) - 1 , arr , count )
        copied = sorted(sorted_arr)
        if not sorted_arr == copied:
            print(-1)
        else:
            print(count[0])
