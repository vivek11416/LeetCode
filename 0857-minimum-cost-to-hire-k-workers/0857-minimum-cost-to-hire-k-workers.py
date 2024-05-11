class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        allRatios = [[wage[i]/quality[i],quality[i]] for i in range(len(quality))]
        allRatios = sorted(allRatios)
        ans = float('inf')
        tot_sum = 0
        max_heap = []
        
        for r,q in allRatios:
            heappush(max_heap,-q)
            tot_sum += q
            
            if len(max_heap) >k:
                tot_sum += heappop(max_heap)
            
            if len(max_heap) ==k:
                ans = min(ans , tot_sum*r)
                
        return ans
   
            
            
        