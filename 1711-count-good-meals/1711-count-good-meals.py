class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = Counter(deliciousness)
        ans = 0
        
        for num in deliciousness:
            freq[num] -= 1
            for i in range(22):
                num2 = (2**i)-num
                
                if num2 in freq:
                    ans += freq[num2]
        
        return ans % (10**9+7)
    

                    
            
        