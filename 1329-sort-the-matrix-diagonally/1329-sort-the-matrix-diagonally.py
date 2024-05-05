class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        maxCol =len(mat[0])
        maxRow = len(mat)
        
        diagInd  = []
        
        for i  in range(maxCol):
            diagInd.append([0,i])
            
        for i  in range(maxRow):
            diagInd.append([i,0])
            
           
        for val in diagInd:
            print(val)
            addR,val = self.return_sorted(val,mat)
            for i,v in enumerate(addR):
                mat[v[0]][v[1]] = val[i]
                
        return mat
            
        
    def return_sorted(self,diagStart,mat):
        maxCol =len(mat[0])
        maxRow = len(mat)
        diag_add  = [diagStart]
        sortedVals = [mat[diagStart[0]][diagStart[1]]]
        row  = diagStart[0]
        col = diagStart[1]

        for i in range(diagStart[0],maxRow-1):
            row += 1
            col += 1
            if  row<=maxRow-1 and col<=maxCol-1:
                diag_add.append([row,col])
                sortedVals.append(mat[row][col])
        x = sorted(sortedVals)    
        return (diag_add,x)
                
            
            
    
        
        
        