class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # Option 1: product of three largest numbers
        product1 = nums[-1] * nums[-2] * nums[-3]

        # Option 2: product of two smallest (negative) numbers
        # and the largest positive number
        product2 = nums[0] * nums[1] * nums[-1]

        return max(product1, product2)