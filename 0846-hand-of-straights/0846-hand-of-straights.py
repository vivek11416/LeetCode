class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        countDict = defaultdict(int)
        for val in hand:
            countDict[val] += 1
            
        allKeys = list(countDict.keys())
        heapq.heapify(allKeys)
        
        while allKeys:
            cur_k = allKeys[0]
            
            for i in range(cur_k,cur_k+groupSize):
                if i not in countDict:
                    return False
                countDict[i] -=1
                
                if countDict[i] == 0:
                    if i != allKeys[0]:
                        return False
                    
                    heapq.heappop(allKeys)
                    
        return True
                    
                    
            
            
        
        