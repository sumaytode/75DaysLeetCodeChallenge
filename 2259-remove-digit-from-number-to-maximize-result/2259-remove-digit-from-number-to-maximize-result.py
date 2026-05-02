class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        temp=0
        for i in range(len(number)):
            if number[i]==digit:
                first_half=number[0:i]
                second_half=number[i+1:]
                final_number=first_half+second_half
                final_Number=int(final_number)
                temp=max(temp, final_Number)
                temp2=str(temp)
        return temp2