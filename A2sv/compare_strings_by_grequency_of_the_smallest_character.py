from collections import Counter
class Solution:
    def search(slef , words , target):
        high = len(words) - 1
        low = 0
        while low <= high:
            mid = (high + low) // 2
            if words[mid] > target :
                high = mid - 1
            elif words[mid] <= target :
                low = mid + 1

        return len(words) - low


    def frequency(slef, string ):
        chars = Counter(string)
        return chars[min(string)]
        
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        for index , val in enumerate(queries) :
            queries[index] = self.frequency(val)
        for index , val in enumerate(words) :
            words[index] = self.frequency(val)

        words.sort()
        ans = []

        for querie in queries:
            ans.append(self.search(words , querie))
        return ans
