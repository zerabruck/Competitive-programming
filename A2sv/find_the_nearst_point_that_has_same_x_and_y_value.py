class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def distance(x1,y1,x2,y2):
            return abs(x1-x2) + abs(y1-y2)

        min_dis=-1
        min_index=-1


        for i,(a,b) in enumerate(points):
            if(a==x or b==y):
                dis=distance(x,y,a,b)
                if(min_dis==-1):
                    min_dis=dis
                    min_index=i
                elif(min_dis>dis):
                    min_dis=dis
                    min_index=i

        return min_index

