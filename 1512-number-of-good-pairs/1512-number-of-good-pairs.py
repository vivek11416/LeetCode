class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gpHashMap = {}
        ans = 0
        
        for num in nums:
            if num in gpHashMap:
                ans += gpHashMap[num]
                gpHashMap[num] += 1
                
            else:
                gpHashMap[num] = 1
                
        return ans