class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=[]
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                arr.append(left+1)
                arr.append(right+1)

                return arr
            elif numbers[left] + numbers[right] > target:
                right = right - 1
             
            else:
                left = left + 1
              