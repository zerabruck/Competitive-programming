class Solution:
    def goUp(self,location,result,mat):
        while(True):
            if location[0] < 0 or location[1] >= len(mat[0]):
                location[0],location[1] = location[0] + 1 , location[1] - 1
                if location[1] + 1 >= len(mat[0]):
                    location[0] = location[0] + 1
                    if location[0] >= len(mat):
                        return [-8,-8] 
                    return location

                location[1] +=1
                return location

            result.append(mat[location[0]] [location[1]])
            location[0],location[1] = location[0] - 1 , location[1] + 1

    def goDown(self,location,result,mat):
        while(True):
            if location[1] < 0 or location[0] >= len(mat):
                
                location[0],location[1] = location[0] - 1 , location[1] + 1

                if location[0] + 1 >= len(mat):
                    location[1] = location[1] + 1 
                    if location[1] >= len(mat[0]):
                        return [-8,-8]
                    return location

                location[0] +=1
                return location

            result.append(mat[location[0]] [location[1]])
            location[0],location[1] = location[0] + 1 , location[1] - 1


    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        size=len(mat)-1
        location=[0,0]
        result=[]
        if len(mat) == 1:
            return mat[0]
 
        while(True):
            value = self.goUp(location,result,mat)
            print("hell")
            if value == [-8,-8] :
                return result

            print(location)
            value=self.goDown(location,result,mat)
            if value == [-8,-8] :
                return result

            print(location)




