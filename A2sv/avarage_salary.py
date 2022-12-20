class Solution:
    def average(self, salary: List[int]) -> float:
        
        sumes=sum(salary)-min(salary)-max(salary)
        return sumes/(len(salary)-2)