class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr=0
        max_sum=0
        i=0
        while i<len(nums):
            if nums[i]==1:
                curr+=1
            else:
                max_sum=max(curr, max_sum)
                curr=0
            i+=1
        max_sum=max(curr, max_sum)
        return max_sum