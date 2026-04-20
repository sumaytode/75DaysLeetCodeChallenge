class Solution:
    def isPalindrome(self, x: int) -> bool:
        u=x
        if x<0:
            return False
        i=0
        t=0
        y=0
        while x!=0:
            d=x%10
            x=x//10
            y=d+(y*10)
            i=i+1

        if u==y:
            return True
        else:
            return False