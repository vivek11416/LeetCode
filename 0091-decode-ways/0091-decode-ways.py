class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        elif s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        else:
            if int(s[:2]) <= 26:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])