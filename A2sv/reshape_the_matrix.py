class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        else:
            reshape = []

            for i in range(r):
                row = [ 0 for i in range(c)]
                reshape.append(row)

            pointer = [0,0]

            for row in mat :
                for col in row :
                    if pointer[1] == c:
                        pointer[0] += 1
                        pointer[1] = 0
                    reshape[pointer[0]][pointer[1]] = col
                    pointer[1] += 1

            return reshape
