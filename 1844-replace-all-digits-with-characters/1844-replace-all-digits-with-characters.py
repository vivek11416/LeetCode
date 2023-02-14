class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        
        def shift(char,num):
            return chr(ord(char)+ int(num)) 
        
        for index in range(len(s)):
            ans += shift(s[index-1],s[index]) if index % 2 else s[index]
            
        return ans
        