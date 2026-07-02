class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b={
            'b':0,
            'a':0,
            'n':0,
            'l':0,
            'o':0
        }

        for i in text:
            if i in b:
                b[i]+=1
            
        small_1= min(b['b'],b['a'],b['n'])
        small_2=min(b['l'],b['o'])
        if b['l']>=2*small_1 and b['o']>=2*small_1:
            return small_1
        elif ((small_2-(small_2%2))/2)<=b['b'] and ((small_2-(small_2%2))/2)<=b['a'] and ((small_2-(small_2%2))/2)<=b['n']:
            return ((small_2-(small_2%2))//2)
        else:
            return 0
        