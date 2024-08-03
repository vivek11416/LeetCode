class Solution:
    def solve(self,arr,k,ind):
        if len(arr)==1:
            return arr[0]
        
        ind = (ind+k)%len(arr)
        arr.pop(ind)
        
        return self.solve(arr,k,ind)
    
    def findTheWinner(self, n: int, k: int) -> int:
#         if n==1 or k==1:
#             return n
        
        person = [i for i in range(1,n+1)]
        k = k-1
        return self.solve(person,k,0)