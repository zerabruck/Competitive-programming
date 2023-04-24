from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingdom = defaultdict(list)
        self.king = kingName
        self.deaths=set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.deaths.add(name)  

    def getInheritanceOrder(self) -> List[str]:
        self.inher_order = []
        self.successor(self.king)
        return self.inher_order

    def successor(self , node):
        if node not in self.deaths:
            self.inher_order.append(node)
        for ele in self.kingdom[node]:
            self.successor(ele)
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
