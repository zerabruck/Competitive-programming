class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # for i in range(k):           
        #     nums.insert(0,nums.pop(-1))
        """
        Do not return anything, modify nums in-place instead.
        """

        
        nums.reverse()
        if k > len(nums):
            k = (k % len(nums))

        beg = 0
        end = k -1
        while(beg <= end):
            nums[beg],nums[end] = nums[end] , nums[beg]
            beg += 1
            end -= 1

    

        beg =  k 
        end = len(nums) - 1

        while(beg <= end):
            nums[beg],nums[end] = nums[end] , nums[beg]
            beg += 1
            end -= 1

        


        






         
        