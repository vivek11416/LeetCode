class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        
        for i in range(1,n):
            if s[i-1]=="0" and s[i] == "0":
                dp[i] = 0
            elif s[i-1]=="0" and s[i] != "0":
                dp[i] = dp [i-1]
            elif s[i-1] !="0" and s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i] = dp[i-2] if i>=2 else 1
                else:
                    dp[i] = 0
            else:
                if int(s[i-1:i+1])<27:
                    dp[i] = dp[i-1]+ (dp[i-2] if i>=2 else 1)
                
                else:
                    dp[i] = dp[i-1]
                    
        return dp[n-1]