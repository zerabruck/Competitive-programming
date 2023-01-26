class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        beg = 0
        end = len(nums) - 1
        count = 0
        nums.sort()

        while(beg < end):
            summed = nums[beg] + nums[end]
            if summed > k:
                end -= 1
            elif summed < k:
                beg += 1

            else:
                beg += 1
                end -= 1
                count += 1

        return count

                
            
                
            
        