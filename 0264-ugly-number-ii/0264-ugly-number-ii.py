class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        factors = [2,3,5]
        visit = set()
        
        for i in range(n):
            num = heapq.heappop(heap)
            if i==n-1:
                return num
            
            for v in factors:
                if num*v not in visit:
                    visit.add(num*v)
                    heapq.heappush(heap,num*v)
                
            