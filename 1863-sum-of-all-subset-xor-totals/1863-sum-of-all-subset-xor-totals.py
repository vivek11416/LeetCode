class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import combinations,accumulate
        
        res = 0
        #[1,2,3,4]
        for i in range(1,len(nums)+1):
            for arr in combinations(nums,i):
                res += list(accumulate(arr,func = lambda x,y : x^y))[-1]
        return res

        