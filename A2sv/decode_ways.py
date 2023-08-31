class Solution:
    def numDecodings(self, s: str) -> int: 
        ele_set = set()
        for i in range(1, 27):
            ele_set.add(str(i))
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        if s[0] in ele_set:
            dp[1] = 1
        for index in range(1, len(s)):
            take_both = s[index - 1] + s[index]
            if take_both in ele_set:
                dp[index + 1] += dp[index - 1]
            if s[index] in ele_set:
                dp[index + 1] += dp[index]
        return dp[-1] 
