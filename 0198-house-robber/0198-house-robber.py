class Solution:
    def rob(self, nums: List[int]) -> int:
        robB,robC = 0,0
        
        for n in nums:
            temp = max(robC,robB+n)
            robB = robC
            robC = temp
            
        return robC