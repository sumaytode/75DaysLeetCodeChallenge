class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lis=[]
        minimum=float('INF')
        maximum=0
        for i in nums:
            if i>maximum:
                maximum=i
            if i<minimum:
                minimum=i

        for j in range(minimum, maximum):
            if j not in nums:
                lis.append(j)

        return lis