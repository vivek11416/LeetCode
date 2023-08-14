class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        rem_len = n-k
        sub_sum = sum(cardPoints[:rem_len])
        
        min_sum = sub_sum
        
        for i in range(rem_len,n):
            sub_sum +=cardPoints[i]
            
            sub_sum -= cardPoints[i - rem_len]
            
            min_sum = min(min_sum,sub_sum)
            
        return total - min_sum
        