from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l,r = 0,0
        length=0
        
        while r < len(s):
            count[s[r]] +=1
            
            if ((r-l+1)-max(count.values()))<=k:
                length = max(length,(r-l+1))
                r += 1
            
            else:
                count[s[l]] -=1
                l+=1
                r +=1
        
        return length
        