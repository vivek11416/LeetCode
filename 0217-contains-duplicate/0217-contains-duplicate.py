class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for v in nums:
            countMap[v] = 1 + countMap.get(v,0)
            if countMap[v]>=2:
                return True
                break
        
        return False
        
        
        