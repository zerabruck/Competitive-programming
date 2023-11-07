class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listing=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>target and nums[j]>0:
                    continue
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    listing.append(i)
                    listing.append(j)
                    return listing
            
                