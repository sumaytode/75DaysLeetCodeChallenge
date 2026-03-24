class Solution:
    def maxArea(self, height: List[int]) -> int:
        mw=0
        left=0
        right=len(height)-1

        while left < right:
            width=right-left
            ht=min(height[left], height[right])

            ans=width*ht
            mw=max(mw,ans)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return mw