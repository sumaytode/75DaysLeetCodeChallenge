class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new=sorted(s)
        final="".join(new)
        few=sorted(t)
        finale="".join(few)

        if final==finale:
            return True
        else:
            return False