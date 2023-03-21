class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ele = []

        self.sub_seq([] , 0)
        return self.ele

    def sub_seq(self, visited , idx):
        if len(self.nums) <= idx:
            return visited       

        visited.append(self.nums[idx])     

        if  len(visited) >= 2 and visited[-1] >= visited[-2] :
            elem = visited.copy()
            if elem not in self.ele:
                self.ele.append(elem)

            self.sub_seq(visited , idx + 1)

        elif len(visited) < 2 :
            self.sub_seq(visited , idx + 1)

        visited.pop()
        self.sub_seq(visited , idx + 1)   
