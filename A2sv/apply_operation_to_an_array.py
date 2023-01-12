class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        operated_arr = []

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0
                operated_arr.append(nums[i])
            elif nums[i] != 0:
                operated_arr.append(nums[i])
        if nums[-1] != 0:
            operated_arr.append(nums[-1])

        operated_arr = operated_arr + [0]* (len(nums)-len(operated_arr))
        return operated_arr

