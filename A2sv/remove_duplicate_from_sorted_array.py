class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 0
        if len(nums) == 1:
            return 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[holder] = nums[i]
                holder += 1
        nums[holder] = nums[-1]

        return holder + 1
