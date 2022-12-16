class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]

        for i in range(len(matrix[0])):
            temp=[]
            for j in matrix:
                temp.append(j[i])

            result.append(temp)

        return result
                