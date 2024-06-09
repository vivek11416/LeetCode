class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remMap = defaultdict(int)
        remMap[0]=1
        ans=0
        preSum = 0
        
        for num in nums:
            preSum += num
            rem = preSum % k
            if rem in remMap:
                ans += remMap[rem]
            remMap[rem] += 1
        return ans
            
     
            
        