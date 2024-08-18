class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2,i3,i5 = 0,0,0
        
        for i in range(1,n):
            min_num = min(
                nums[i2]*2,nums[i3]*3,nums[i5]*5,
            )
            nums.append(min_num)
            if min_num == nums[i2]*2:
                i2 += 1
                
            if min_num == nums[i3]*3:
                i3 += 1
                
            if min_num == nums[i5]*5:
                i5 += 1
                
        return nums[n-1]
        
#         heap = [1]
#         factors = [2,3,5]
#         visit = set()
        
#         for i in range(n):
#             num = heapq.heappop(heap)
#             if i==n-1:
#                 return num
            
#             for v in factors:
#                 if num*v not in visit:
#                     visit.add(num*v)
#                     heapq.heappush(heap,num*v)
                
            