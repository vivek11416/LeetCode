class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heappush(heap,-1*num)
            
        initialSum = sum(nums)
        targetSum = sum(nums)/2
        k=0
        
        while initialSum > targetSum:
            val = heappop(heap)
            heappush(heap,val/2)
            initialSum -= (-1 * (val/2))
            k = k + 1
            
        return k
            
        