class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = -inf
        dp = []
        for _ in range(m):
            dp.append([-inf]*n)
            
        dp[0][0] = 0
        
        for i in range(m):
            for j in range(n):
                
                if i==0 and j==0:
                    continue
                
                if j-1 >= 0:
                    c2 = grid[i][j]
                    c1 = grid[i][j-1]
                    optimalPathFromLeft = dp[i][j-1]
                    dp[i][j] = max(c2-c1,c2-c1+optimalPathFromLeft)
                    
                if i-1 >= 0:
                    c2 = grid[i][j]
                    c1 = grid[i-1][j]
                    optimalPathFromUp = dp[i-1][j]
                    dp[i][j] = max(dp[i][j],c2-c1,c2-c1+optimalPathFromUp)
                    
                ans = max(ans,dp[i][j])
                
        return ans