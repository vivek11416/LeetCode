class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    
    def helper(self,nums):
        robB,robC = 0,0
        for n in nums:
            temp = max(robC,robB+n)
            robB = robC
            robC = temp

        return robC
        