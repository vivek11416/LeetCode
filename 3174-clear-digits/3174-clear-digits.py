class Solution:
    def clearDigits(self, s: str) -> str:
        heap = []
        s  =list(s)
        
        for i,v in enumerate(s):
            if v.isalpha():
                heapq.heappush(heap,-i)
            
            else:
                heapq.heappop(heap)
                
        ansList = []
        while heap:
            j = heapq.heappop(heap)
            ansList.append(s[-j])
        
        return "".join(ansList[::-1])
                