class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        elements_palces = {}

        for index,value in enumerate(nums):
            elements_palces[value] = index
        for place,replace in operations:
            index = elements_palces[place]
            nums[index] = replace
            elements_palces[replace] = index

        return nums

