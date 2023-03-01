class Solution:
    def reverse(self,s,ptr):
        if ptr == len(s) // 2:
            return

        s[ptr] , s[~ptr] = s[~ptr] , s[ptr]
        self.reverse(s,ptr + 1)
        return 

    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr = 0
        self.reverse(s,ptr)
