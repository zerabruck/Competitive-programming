class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        def go_right(matrix):
            value=matrix.pop(0)
            for i in value:
                result.append(i)

        def go_down(matrix):
            for i in matrix:
                result.append(i[-1])
                i.pop(-1)
        def go_left(matrix):

            matrix.reverse()
            matrix[0].reverse()
            go_right(matrix)
            matrix.reverse()

        def go_up(matrix):
            matrix.reverse()
            for i in matrix:
                result.append(i[0])
                i.pop(0)
            matrix.reverse()



        while(True):
            try:
                go_right(matrix)
                go_down(matrix)
                go_left(matrix)
                go_up(matrix)
            except:
                break
        return result
