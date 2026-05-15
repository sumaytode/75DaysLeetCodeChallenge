class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minimum=float('inf')
        if len(nums)==1:
            return nums[0]
        while l<=r:
            minimum=min(minimum,nums[l],nums[r])
            l+=1
            r-=1
        return minimum

        