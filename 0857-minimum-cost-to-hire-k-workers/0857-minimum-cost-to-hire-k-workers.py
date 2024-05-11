class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(quality)
        worker=[[w/q, q] for w, q in zip(wage, quality)]

        worker.sort()
        quality_sum=0
        heap=[]

        for ratio, q in worker[:k]:
            quality_sum+=q
            heappush(heap, -q)
        pay=worker[k-1][0]*quality_sum

        for ratio, q in worker[k:n]:
            heappush(heap, -q)
            quality_sum+=q+heappop(heap)
            pay=min(pay, quality_sum*ratio)

        return pay
        
        
        
        
        
        
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
                    
                
                
                
                
            
            
        