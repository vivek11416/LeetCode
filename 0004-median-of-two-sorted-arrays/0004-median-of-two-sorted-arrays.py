class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        totLen = len(nums1)+len(nums2)
        mid = totLen//2
        
        if len(B)<len(A):
            A,B = B,A
        
        l,r = 0, len(A)-1
        while True:
            
            
            mA = (l+r)//2
            mB = mid - mA -2
            
            
            leftA = A[mA] if mA >= 0 else float('-infinity')
            rightA = A[mA + 1] if (mA + 1) <= len(A)-1 else float('infinity')
            leftB = B[mB] if mB >= 0 else float('-infinity')
            rightB = B[mB + 1] if (mB + 1) <= len(B)-1 else float('infinity')
            
            
            if leftA <= rightB and leftB <= rightA :
                if totLen % 2>0:
                    return min(rightB,rightA)
                else:
                    return (max(leftB,leftA)+min(rightB,rightA))/2
                
                    
            
            elif leftA > rightB:
                r = mA - 1
            
            else:
                l = mA + 1
                
            
        