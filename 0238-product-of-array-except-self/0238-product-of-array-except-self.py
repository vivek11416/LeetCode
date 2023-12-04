class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        ans = [1]*len(nums)
        
        
        for i in range(len(nums)):
            ans[i] =  ans[i] * pre
            pre *= nums[i]
         
        for i in range(len(nums)-1,-1,-1):
            ans[i] =  ans[i] * post
            post *= nums[i]
            
        return ans