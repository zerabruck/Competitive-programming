class Solution:
    def is_predecessor(self, pred, word):
        first = 0
        second = 0
        while first < len(pred) and second < len(word):
            if pred[first] == word[second]:
                first += 1
                second += 1
            else:
                second += 1
        if first == len(pred):
            return True
        return False
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        dp = [0] * len(words)
        dp[0] = 1
        for index in range(1, len(words)):
            for prev in range(index - 1, -1, -1):
                if len(words[index]) - len(words[prev]) == 1 and self.is_predecessor(words[prev], words[index]):
                    dp[index] = max(dp[index], dp[prev])
            dp[index] += 1
        return max(dp)  
