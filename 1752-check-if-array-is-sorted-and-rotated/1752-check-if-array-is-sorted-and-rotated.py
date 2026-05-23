class Solution:
    def check(self, nums: List[int]) -> bool:
        break_count = 0
        for i, current_value in enumerate(nums):
            if nums[i - 1] > current_value:
                break_count += 1
      
        return break_count <= 1