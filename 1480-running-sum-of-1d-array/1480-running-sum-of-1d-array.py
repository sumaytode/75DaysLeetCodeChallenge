class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        count=0
        result=[]
        for i in nums:
            count=count+i
            result.append(count)

        return result