class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1:
                ans.append((digits[i]+1+carry)%10)
                carry = (digits[i]+1+carry)//10
            else:
                ans.append((digits[i]+carry)%10)
                carry = (digits[i]+carry)//10
            
        if carry!=0:
            ans.append(carry)
            
        return ans[::-1]
            
            
        