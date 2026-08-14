class Solution:
    def isPalindrome(self, s: str) -> bool:
        list=[]
        for i in s:
            if i.isalnum():
                list.append(i.lower())

        sttr=''.join(list)
        if sttr==sttr[::-1]:
            return True
        else:
            return False