class Solution:
    def sube_seq(self, word, places):
        curr = 0
        for symbol in word:
            ind = bisect_left(places[symbol], curr)
            if ind >= len(places[symbol]):
                return False
            curr = places[symbol][ind] + 1
        
        return True
    def numMatchingSubseq(self, S, words):
        
        
        places = defaultdict(list)
        for index, symbol in enumerate(S):
            places[symbol].append(index)

        val = 0
        for word in words:
            val += self.sube_seq(word, places)
        
        return val
