class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0]*n
        
        maxVal = float("-inf")
        
        for i in range(n-1,-1,-1):
            dp[i]  =  energy[i] + (dp[i+k] if i+k < n else 0)
            maxVal = max(maxVal,dp[i])
        
        return maxVal
        
        
        
#         brute Force (Times Out)
#         allValidIndex=[]
#         for i in range(0,len(energy),k):
#             allValidIndex.append(i)
            
#         maxSum = float('-inf')   
#         for i in range(len(energy)):
#             tempSum = 0
#             for j in allValidIndex:
#                 try:
#                     tempSum += energy[i+j]
#                 except:
#                     pass
#             maxSum = max(tempSum,maxSum)
        
#         return maxSum
            
        