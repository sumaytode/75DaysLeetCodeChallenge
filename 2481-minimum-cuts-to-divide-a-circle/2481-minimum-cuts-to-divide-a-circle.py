class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n%2==0 and n>=2:
            return n//2
        elif n%2!=0 and n>2:
            return n
        else:
            return 0