class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=[]

        # Mark visited indices
        for i in range(len(nums)):
            idx= abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Find missing numbers
        for i in range(len(nums)):
            if nums[i] > 0:
                arr.append(i + 1)

        return arr