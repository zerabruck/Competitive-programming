class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.value = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
                curr.children[index].value = char
            curr = curr.children[index]
        curr.is_end = True
        curr.value = word[-1]

    def longest_word(self, node):
        char = ''
        flag = False
        for index in range(26):
            if node.children[index] and node.children[index].is_end:
                flag = True
                val = self.longest_word(node.children[index])
                if len(val) > len(char):
                    char = val
        if not flag:
            return node.value
        return node.value + char

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.longest_word(trie.root)
