class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = 1
        max_coins = 0
        divided = len(piles) // 3 
        for i in range(divided):
            max_coins += piles[n]
            n += 2
        return max_coins


