class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n%2 == 0:
            for i in range(n//2):
                ans.append(i+1)
                ans.append(-(i+1))
                
        else:
            ans.append(0)
            for i in range(n//2):
                ans.append(i+1)
                ans.append(-(i+1))
                
        return ans
            
                
        