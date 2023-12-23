class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,v in enumerate(nums):
            
            if i>0 and v==nums[i-1]:
                continue
            
            l,r = i+1 ,len(nums)-1
            
            while l<r:
                
                if (v + nums[l]+nums[r])>0:
                    r = r-1
                    
                elif (v + nums[l]+nums[r])<0:
                    l = l+1
                    
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                        
        
        return res
                
        