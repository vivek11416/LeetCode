class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gpHashmap={}
        ans = 0
        for num in nums:
            if num in gpHashmap:
                ans += gpHashmap[num]
                gpHashmap[num] += 1
            else:
                gpHashmap[num] = 1
        
        return ans
                