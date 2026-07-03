class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx=0
        curr=0

        for i in gain:
            curr=curr+i
            mx=max(mx,curr)
        return mx