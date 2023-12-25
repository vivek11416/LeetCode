class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        freqList = [[] for x in range(len(nums)+1)]
        
        for i in nums :
            countDict[i] = 1 + countDict.get(i,0)
            
        for c,v in countDict.items():
            freqList[v].append(c)
        ans = []   
        for i in range(len(freqList)-1,0,-1):
            for n in freqList[i]:
                ans.append(n)
                
                if len(ans)==k:
                    return ans
        
        
