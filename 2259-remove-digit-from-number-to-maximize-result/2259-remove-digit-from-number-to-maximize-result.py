class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        temp=0
        for i in range(len(number)):
            if number[i]==digit:
                temp=max(temp, int(number[0:i]+number[i+1:]))
        return str(temp)