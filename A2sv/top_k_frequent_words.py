from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ele_count = Counter(words)
        freqs = []
        for key, val in ele_count.items():
            heapq.heappush(freqs, (-val,key))
        res = []
        while len(res) < k:
            val = heapq.heappop(freqs)
            res.append(val[1])
        return res
