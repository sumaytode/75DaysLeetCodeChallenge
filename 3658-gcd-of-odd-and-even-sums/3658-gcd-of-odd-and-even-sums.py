class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd=0
        sumeven=0

        for i in range(1,(n*2)+1):
            if i%2==0:
                sumeven+=i
            else:
                sumodd+=i
                
        for j in range(n,0,-1):
            if sumodd%j==0 and sumeven%j==0:
                return j
