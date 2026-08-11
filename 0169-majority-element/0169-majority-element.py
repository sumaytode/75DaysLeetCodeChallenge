class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = dict()              # stores frequency of each number
        n = len(nums)

        # Build frequency table
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        # Find the element with frequency > n//2
        for k, v in hash_map.items():
            if v > n // 2:
                return k