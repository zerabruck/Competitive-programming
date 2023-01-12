class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        unsorted = 0
        

        for col in range(len(strs[0])):
            column = [ele[col] for ele in strs]

            sorted_column = sorted(column)
            if column != sorted_column :
                unsorted += 1

        return unsorted

        
