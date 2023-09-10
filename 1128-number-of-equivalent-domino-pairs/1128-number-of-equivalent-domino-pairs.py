class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        count= {}
        ans = 0
        
        for val in dominoes:
            if str(val) in count or str(val[::-1]) in count:
                try:
                    count[str(val)] += 1
                    
                except:
                    try:
                        count[str(val[::-1])] += 1
                    except:
                        pass
                    
            else:
                count[str(val)] = 1
                
        for _,v in count.items():
            ans += (v*(v-1))//2
        return ans
                    
