class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        st1=[]
        for i in words:
            st1.append(i[0])
        if "".join(st1) == s:
            return True
        else:
            return False