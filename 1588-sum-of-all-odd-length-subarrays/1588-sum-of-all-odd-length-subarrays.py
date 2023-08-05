class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = sum(arr)
        
        for i in range(3,len(arr)+1,2):
            for j in range(len(arr)):
                if(i+j)>len(arr):
                    break
                else:
                    total += sum(arr[j:i+j])
        return total
        
        