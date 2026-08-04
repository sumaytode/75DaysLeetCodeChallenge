class Solution:
    def maxProduct(self, n: int) -> int:
        lis=[]
        for i in range(len(str(n))):
            remainder= n%10
            n=n//10
            lis.append(remainder)

        lis_sort=sorted(lis)
        return lis_sort[-1] * lis_sort[-2]