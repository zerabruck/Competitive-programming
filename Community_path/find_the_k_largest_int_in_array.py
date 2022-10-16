class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        new=[int(i) for i in nums]
        new.sort(reverse=True)
        
        return str(new[k-1])
            
                
        