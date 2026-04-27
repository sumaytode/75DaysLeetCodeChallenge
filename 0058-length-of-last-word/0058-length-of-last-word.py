class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=s.strip().split()[-1]
        return len(n)