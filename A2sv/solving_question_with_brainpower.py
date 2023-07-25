class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        max_q = 0
        for index in range(len(questions) - 1, -1, -1):
            value = questions[index][0]
            jump = questions[index][1] + index + 1
            if jump < len(dp):
                value += dp[jump]
            if index + 1 < len(dp):
                value = max(value, dp[index + 1])
            max_q = max(max_q, value)
            dp[index] = value
        return max_q
