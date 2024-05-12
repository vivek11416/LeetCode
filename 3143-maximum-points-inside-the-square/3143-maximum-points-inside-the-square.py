class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int: 
        positionMap =defaultdict(list)
        listStr =list(s)
        
        for i,val in enumerate(points):
            key = max(abs(val[0]),abs(val[1]))
            positionMap[key].append(listStr[i])
        
        positionMap=dict(sorted(positionMap.items()))
        print(positionMap)
        visited = set()
        total =  0
        for k,v in positionMap.items():
            prevLen = len(visited)
            visited.update(v)
            if  len(set(v))==len(v) and prevLen+len(v) ==  len(visited) :
                
                total +=len(v)
            else:
                return total
            
        return total
                