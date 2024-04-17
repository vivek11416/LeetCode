class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import defaultdict 
        ans = defaultdict(int)
        for val in nums:
            if ans[val] == 0:
                ans[val] += 1
            else:
                ans[val] -= 1
                
        return len(set(ans.values())) == 1 and list(ans.values())[0]==0
            
        
        
        