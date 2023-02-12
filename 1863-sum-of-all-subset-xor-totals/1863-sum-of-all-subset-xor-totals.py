class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import combinations, accumulate

        res = 0
        for i in range(1, len(nums)+1):  # Iterate through all lengths of subsets
            for arr in combinations(nums, i):  # Sum up the XOR results
                res += list(accumulate(arr, func=lambda x, y: x ^ y))[-1]
        return res
