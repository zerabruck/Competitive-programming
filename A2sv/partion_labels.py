from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        ele_set = set()
        ele_dict = Counter(s)

        beg = 0
        count = 0
        partitions = []

        for end,value in enumerate(s) :
            if value not in ele_set:
                count += ele_dict[value]
                ele_set.add(value)

            count -= 1
            if count == 0:
                value = (end - beg) + 1
                partitions.append(value)
                beg = end + 1


        return partitions





        
          
                