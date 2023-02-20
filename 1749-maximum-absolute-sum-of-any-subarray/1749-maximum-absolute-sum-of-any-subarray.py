class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxV,minV,res= 0,0,0
        
        for a in nums:
            maxV = max(a,maxV+a)
            minV = min(a,minV+a)
            res = max(res,maxV,-minV)
        return res
        