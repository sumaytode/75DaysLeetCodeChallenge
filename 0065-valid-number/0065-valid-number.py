class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        digit_after_e = True
        
        for i in range(len(s)):
            
            if s[i].isdigit():
                seen_digit = True
                digit_after_e = True
            
            elif s[i] == '+' or s[i] == '-':
                # sign only allowed at start or after e/E
                if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            
            elif s[i] == '.':
                # only one dot and not after e
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            
            elif s[i] == 'e' or s[i] == 'E':
                # only one e and must have number before it
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                digit_after_e = False
            
            else:
                return False
        
        return seen_digit and digit_after_e