class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminderMap = {0:-1}
        tot = 0
        
        for i,n in enumerate(nums):
            tot += n
            rem =tot %k
            if rem not  in reminderMap:
                reminderMap[rem] = i
                
            elif abs(reminderMap[rem] - i) >1:
                return True
        
        return False
        