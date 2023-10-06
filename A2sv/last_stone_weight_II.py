class Solution:
    def combination(self, index, total):
        if index >= len(self.stones):
            return 0

        if index not in self.dp:
            choose =  self.combination(index + 1, total + self.stones[index])
            not_choose = self.combination(index + 1)

            diff1 = self.total - choose
            diff2 = self.total - not_choose

            resul1 = max(diff1, choose) - min(diff1, choose)
            resul2 = max(diff2, not_choose) - min(diff2, not_choose)

            self.dp[index] = min(resul1, resul2)

        return self.dp[index]
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums = sum(stones)
        dp = [[0]*(sums//2+1) for _ in range(len(stones)+1)]
        for i in range(1, len(stones)+1):
            for j in range(1, sums//2+1):
                if stones[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], stones[i-1]+dp[i-1][j-stones[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        return sums - 2 * dp[len(stones)][-1]
        
