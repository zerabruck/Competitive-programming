input()
first_arr = list(map(int,input().split()))
second_arr = list(map(int,input().split()))

sec_pointer = 0
nums = []

for index,value in enumerate(first_arr):
    if value > second_arr[sec_pointer]:
        nums.append(index + 1)
        sec_pointer += 1

    
differ = len(second_arr) - 1 - sec_pointer



