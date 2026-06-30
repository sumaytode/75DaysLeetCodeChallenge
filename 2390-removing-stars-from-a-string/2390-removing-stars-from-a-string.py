class Solution:
    def removeStars(self, s: str) -> str:
        stck=[]
        for i in s:
            if i!='*':
                stck.append(i)
            else:
                stck.pop(len(stck)-1)
        return ''.join(stck)