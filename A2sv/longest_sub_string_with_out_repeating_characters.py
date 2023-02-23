class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        max_length = 0
        start = 0
        for end in range(len(s)):         
            while s[end] in sets:
                sets.remove(s[start])
                start += 1

            sets.add(s[end])
            max_length = max(max_length , (end - start) + 1)

        return max_length
