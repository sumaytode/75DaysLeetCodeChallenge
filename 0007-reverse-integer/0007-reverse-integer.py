class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            X=x*-1
        else:
            X=x*1
        t=X
        y=0
        while X!=0:
            d=X%10
            X=X//10
            y=d+(y*10)
        
        # Apply sign
        if x < 0:
            y = -y
        
        # Now check overflow (IMPORTANT)
        if y < -2**31 or y > 2**31 - 1:
            return 0
        
        return y