class Solution:
    def isThree(self, n: int) -> bool:
        totalDiv = 2
        
        for i in range(2,n):
            if n%i == 0:
                totalDiv +=1
        return totalDiv == 3
            
        
        