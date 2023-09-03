class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = j = 0
        n = len(s)
        op = 0
        seen = {'a':0,'b':0,'c':0}
        
        while i+3<=n:
            if seen['a']>=1 and seen['b']>=1 and seen['c']>=1:
                seen[s[i]] -= 1
                op += n-j+1
                i+=1
                
            else:
                if j <=n-1:
                    seen[s[j]] += 1
                    j +=1
                else:
                    break
                    
        return op
                    
        