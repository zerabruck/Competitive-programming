class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.value = 0
        self.children_value = 0
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.keys = {
        }
    
    def insert(self, key: str, val: int) -> None:
        if key in self.keys:
            val = val - self.keys[key]

        curr = self.root
        for char in key:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr.children_value += val
            curr = curr.children[index]
        curr.value += val
        self.keys[key] = curr.value

    def sum(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not current.children[index]:
                return 0

            current = current.children[index]

        return current.value + current.children_value

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
