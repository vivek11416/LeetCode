class Solution:
    def generateTheString(self, n: int) -> str:
        return ''.join(['p'*(n-1) ,'z'*1])if n%2==0 else ''.join(['p'*n])
        