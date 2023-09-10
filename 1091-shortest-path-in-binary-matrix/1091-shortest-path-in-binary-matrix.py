class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        if grid == [[0]]:
            return 1
        
        q = [(0,0,1)]
        
        grid[0][0] = 1
        
        
        while q :
            x ,y ,length = q.pop(0)
            
            for nextX in [x-1,x,x+1]:
                for nextY in [y-1,y,y+1]:
                    if nextX == len(grid) -1 and nextY ==len(grid[0]) - 1:
                        return length + 1
                    
                    if nextX >= 0 and nextX < len(grid) and nextY >= 0 and nextY < len(grid[0]):
                        if grid[nextX][nextY] == 0:
                            q.append((nextX,nextY,length+1))
                            grid[nextX][nextY] = 1
                        
        return -1
                        