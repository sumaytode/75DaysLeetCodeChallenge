class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=''
        cnt=0
        for i in str(n):
            if i!='0':
                s=s+i
                cnt=cnt+int(i)
        
        if s=='':
            return 0
        else:
            return int(s) * cnt