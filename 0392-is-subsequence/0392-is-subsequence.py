class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = -1

        for i in range(len(s)):
            found = False

            for j in range(count + 1, len(t)):
                if s[i] == t[j]:
                    count = j
                    found = True
                    break

            if not found:
                return False

        return True