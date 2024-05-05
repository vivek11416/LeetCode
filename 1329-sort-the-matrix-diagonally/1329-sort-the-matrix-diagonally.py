class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        self.maxCol =len(mat[0])
        self.maxRow = len(mat)
        
        diagInd  = []
        
        for i  in range(self.maxCol):
            diagInd.append([0,i])
            
        for i  in range(self.maxRow):
            diagInd.append([i,0])
            
           
        for val in diagInd:
            addR,val = self.return_sorted(val,mat)
            for i,v in enumerate(addR):
                mat[v[0]][v[1]] = val[i]
                
        return mat
            
        
    def return_sorted(self,diagStart,mat):
        diag_add  = [diagStart]
        sortedVals = [mat[diagStart[0]][diagStart[1]]]
        row  = diagStart[0]
        col = diagStart[1]

        for i in range(diagStart[0],self.maxRow-1):
            row += 1
            col += 1
            if  row<=self.maxRow-1 and col<=self.maxCol-1:
                diag_add.append([row,col])
                sortedVals.append(mat[row][col])
        x = sorted(sortedVals)    
        return (diag_add,x)
                
            
            
    
        
        
        