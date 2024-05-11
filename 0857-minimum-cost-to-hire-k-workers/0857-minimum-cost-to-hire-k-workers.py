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
            
            

        
        
        
        
        
        
#         import itertools
# #         allComb = []
# #         for comb in itertools.permutations([i for i in range(len(quality))], k):
# #             allComb.append(comb)
            
# #         # for  val  in allComb:
# #         #     allComb.append(val[::-1])
            
#         minPrice=float('inf')  

#         for val in itertools.permutations([i for i in range(len(quality))], k):
#             ratio = wage[val[0]]/quality[val[0]]
#             totalPrice = wage[val[0]]
            
#             for i in range(1,len(val)):
#                 if wage[val[i]]<=quality[val[i]]*ratio:

#                     totalPrice+=quality[val[i]]*ratio
                    
#                 else:
#                     totalPrice  +=float('inf')  
            
#             # print( min(minPrice,totalPrice))
#             minPrice= min(minPrice,totalPrice)
            
#         return minPrice
                    
                
                
                
                
            
            
        