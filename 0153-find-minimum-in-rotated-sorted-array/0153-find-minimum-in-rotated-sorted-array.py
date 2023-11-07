class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l,r=0,len(nums)-1
        
        if nums[l] < nums[r]:
            return ans
        
        while l<=r:
            if nums[l] < nums[r]:
                ans = min(nums[l],ans)
                return ans
            
            
            mid = (l+r)//2
            ans = min(ans,nums[mid])
            
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r=mid-1
        
        return ans