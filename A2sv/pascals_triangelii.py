class Solution:
    def pascal_triangle(self,row ,ele):
        
        if row == 0:
            return ele

        new_ele = [1] 
        for el in range(1,len(ele)):
            val = ele[el] + ele[el - 1]
            new_ele.append(val)
        new_ele.append(1)
        return self.pascal_triangle(row - 1 , new_ele)


    def getRow(self, rowIndex: int) -> List[int]:
        return self.pascal_triangle(rowIndex,[1])
