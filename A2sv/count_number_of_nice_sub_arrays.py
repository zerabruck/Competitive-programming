from collections import deque
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        queue = deque()
        left = 0
        temp = 0
        first_odd = -1
        sub_arrays = 0
        for right in range(len(nums)) :
            if nums[right] % 2 != 0 :
                temp += 1
                queue.append(right)
            if temp > k :
                while nums[left] % 2 == 0  :
                    left += 1    
                left += 1
                temp -= 1
                queue.popleft()

            if temp == k :
                val = queue[0] - left + 1
                sub_arrays += val

        return sub_arrays 
