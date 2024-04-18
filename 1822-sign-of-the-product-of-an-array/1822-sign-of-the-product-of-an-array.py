class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for val in nums:
            prod *= val
            
        if prod == 0:
            return 0
        elif prod < 0:
            return -1
        else:
            return 1
            
            
        