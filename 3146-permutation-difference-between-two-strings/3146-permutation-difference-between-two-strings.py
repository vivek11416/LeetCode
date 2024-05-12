class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sMap = {}
        for i,val in enumerate(list(s)):
            sMap[val]=i
            
        totSum=0  
        
        for i , val in enumerate(list(t)):
            totSum +=  abs(i - sMap[val])
            
        return totSum
            
            
        