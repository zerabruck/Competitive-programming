import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.largest) > k:
            heapq.heappop(self.largest)       

    def add(self, val: int) -> int:
        if len(self.largest) < self.k:
            heapq.heappush(self.largest, val)
        elif self.largest[0] < val:
            heappop(self.largest)
            heappush(self.largest, val) 
        return self.largest[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
