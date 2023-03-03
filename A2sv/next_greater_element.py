class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dec_stack = []
        gre_ele = [-1] * len(nums)
        
        for num in range(len(nums) * 2 ):
            num = num % len(nums)
            if len(dec_stack) == 0:
                dec_stack.append(num)

            elif nums[dec_stack[-1]] >= nums[num]:
                dec_stack.append(num)

            elif nums[dec_stack[-1]] < nums[num]:
                while dec_stack and nums[dec_stack[-1]] < nums[num]:
                    val = dec_stack.pop()
                    gre_ele[val % len(nums)] = nums[num]

                dec_stack.append(num)

        return gre_ele 
