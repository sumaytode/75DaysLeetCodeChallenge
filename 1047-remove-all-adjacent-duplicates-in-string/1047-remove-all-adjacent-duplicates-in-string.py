class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):

            if not stack:
                stack.append(s[i])
            elif s[i]!=stack[-1]:
                stack.append(s[i])
            else:
                stack.pop(-1)
            
        return "".join(stack)
            