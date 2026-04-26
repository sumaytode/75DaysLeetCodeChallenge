class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n=len(nums)

        left_max=[0]*n
        left_max[0]=nums[0]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1],nums[i])
        
        right_max=[0]*n
        right_max[n-1]=nums[n-1]
        for i in range(n-2,1,-1):
            right_max[i]=max(right_max[i+1],nums[i])

        result=[]
        for i in range(n):
            if i==0 or i==n-1 or nums[i] > left_max[i-1] or nums[i] > right_max[i+1]:
                result.append(nums[i])

        return result