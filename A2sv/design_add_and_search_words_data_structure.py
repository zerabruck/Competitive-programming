class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.value = ''

class WordDictionary:
    def __init__(self):
        self.curr = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.curr
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
                current.children[index].value = char

            current = current.children[index]
        current.is_end = True  

    def search(self, word: str) -> bool:
        self.word = word
        return self.go_through(0, self.curr)

    def go_through(self, index, node):
        if index >= len(self.word):
            return False
        child_index = ord(self.word[index]) - ord('a')
        children = node.children

        if index == len(self.word) - 1:
            if self.word[index] == '.':
                for child in children:
                    if child and child.is_end:
                        return True

            elif children[child_index]:
                return children[child_index].is_end 
      
        elif self.word[index] == ".":
            val = False
            for child in children:
                if child:
                    val = self.go_through(index + 1, child)
                    if val:
                        return True
        elif children[child_index]:
            return self.go_through(index + 1, children[child_index])
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
