class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        values=[]
        nums.sort()
        for i in range(len(nums)):
            if(target==nums[i]):
                values.append(i)
        return values
                

        