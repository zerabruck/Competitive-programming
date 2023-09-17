class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        bfs = deque() 
        max_count = 0
        for index in range(len(nums)):
            if index not in visited:
                count = 1
                temp = nums[index]
                while index != temp:
                    visited.add(temp)
                    temp = nums[temp]
                    count += 1
                max_count = max(max_count, count)
        return max_count
