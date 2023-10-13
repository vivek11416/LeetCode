class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return [1]
        elif len(nums)==0:
            return [0]
        elif len(set(nums))==1:
            return[nums[0]]
        
        count = defaultdict(int)
        ans = []
        
        for i in nums:
            count[i] += 1
            

        keys = list(count.keys())
        values = list(count.values())
        
        for i in range(k):
            ans.append(keys[values.index(max(values))])
            tInd = values.index(max(values))
            values.pop(tInd)
            keys.pop(tInd)
  
        return ans