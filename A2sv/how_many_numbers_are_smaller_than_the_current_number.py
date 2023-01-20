class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        result = [ ]

        for num in nums:
            index = ordered.index(num) 
            result.append(index)

        return result
  

        


