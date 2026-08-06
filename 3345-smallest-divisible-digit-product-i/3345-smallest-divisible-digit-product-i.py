class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            prob=1
            for j in range(len(str(i))):
                prob=prob*int(str(i)[j])
            if prob%t==0:
                break
        return i

    