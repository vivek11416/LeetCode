class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums) * 2
        
        lenVal = len(nums)
        
        for i in range(len(nums)):
            res[i] = res[i+lenVal] = nums[i]
            
        return res
        
        