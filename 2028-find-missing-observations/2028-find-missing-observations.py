class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        expectedSum = ((len(rolls) + n) * mean ) - sum(rolls)
        
        if n>expectedSum or expectedSum> 6*n:
            return []
        
        ans = []
        
        while n:
            val = expectedSum//n
            ans.append(val)
            expectedSum -= val
            n -= 1 
        return ans
                
        
        