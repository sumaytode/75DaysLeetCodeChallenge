class Solution:
    def secondHighest(self, s: str) -> int:
        integer=[]
        for i in s:
            if i.isdigit() and int(i) not in integer:
                integer.append(int(i))
        integer.sort()
        if len(integer)==1 or len(integer)==0:
            return -1
        else:
            return integer[-2]