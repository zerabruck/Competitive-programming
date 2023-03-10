class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sets = [[]]
        self.nums = nums
        self.all_sets( [] , 0)
        return self.sets

    def all_sets(self , visited , idx):
        if idx >= len(self.nums) :
            return 

        visited.append(self.nums[idx])
        val = visited.copy()
        self.sets.append(val)   
        self.all_sets(visited , idx + 1 )

        visited.pop()
        self.all_sets(visited , idx + 1 )
