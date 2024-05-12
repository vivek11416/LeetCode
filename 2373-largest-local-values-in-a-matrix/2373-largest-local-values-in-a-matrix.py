class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        allMatCor  =  []
        maxCol = len(grid[0])-2
        maxRow = len(grid) - 2
        maxVal = []
        updatedVal =[]
        for i in range(maxRow):
            for j in range(maxCol):
                allMatCor.append([[i,j],[i+2,j+2]])
                
        for val in allMatCor:
            tempMax = -1
            for i in range(val[0][0],val[1][0]+1):
                for  j in range(val[0][1],val[1][1]+1):
                    tempMax = max(tempMax,grid[i][j])
            
            maxVal.append(tempMax)
        print(maxVal,maxCol)
        
        for _ in range(len(maxVal)):
            temp = []
            if len(maxVal)>0:
                for j in range(maxCol):
                    temp.append(maxVal.pop(0))
                
                updatedVal.append(temp)
        return updatedVal
        

        
            
        