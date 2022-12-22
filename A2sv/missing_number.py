class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sets=set(nums)
        all_numb=[x for x in range(len(nums)+1)]
        for i in all_numb:
            if(i not in sets):
                return i