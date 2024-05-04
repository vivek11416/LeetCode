class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans = mask = 0
        seen = {0: -1}
        
        for i,c in enumerate(s):
            
            if c in "aeiou":
                mask ^= 1 << ('aeiou'.find(c))
            
            if mask in seen:
                ans =  max(ans,i-seen[mask])
                
            seen.setdefault(mask,i)
            
        return ans
                
                
            