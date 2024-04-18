class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        converted = []
        for val in list(s):
            converted.append(str(ord(val)-96))
            
        ans = int(''.join(converted))
        
        for i in range(k):
            temp = 0
            ans = list(str(ans))
            for val in ans:
                temp = temp + int(val)
            
            ans = temp
            
        return ans
            
            
            
        
        
        