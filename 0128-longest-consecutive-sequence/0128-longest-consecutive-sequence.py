class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0
        
        for val in setNums:
            if val-1 not in setNums:
                length = 1
                
                while val + length in setNums:
                    length += 1
                    
                
                longest = max(length,longest)
                
        return longest
            
        