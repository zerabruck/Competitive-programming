class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        if(num==num[::-1]):
            return True

        return False
        