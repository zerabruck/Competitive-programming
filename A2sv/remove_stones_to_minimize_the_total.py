import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        for i in range(k):
            val = heapq.heappop(piles)
            sub = int(val / 2)
            val -= sub
            heapq.heappush(piles, val)
        sums = sum(piles)
        return -sums
