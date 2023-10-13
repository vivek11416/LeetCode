class Solution:
    def isPalindrome(self, s: str) -> bool:
        charList = list(s.lower())
        
        ans = []
        
        for val in charList:
            if val.isalnum():
                ans.append(val)
        
        return ans == ans[::-1]
        