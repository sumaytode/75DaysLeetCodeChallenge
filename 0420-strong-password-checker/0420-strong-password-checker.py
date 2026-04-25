class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        upper = any(c.isupper() for c in password)
        lower = any(c.islower() for c in password)
        digit = any(c.isdigit() for c in password)
        
        missing = int(not upper) + int(not lower) + int(not digit)
        
        replace = 0
        one = two = 0
        
        i = 0
        while i < n:
            j = i
            while i < n and password[i] == password[j]:
                i += 1
            length = i - j
            
            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
        
        if n < 6:
            return max(missing, 6 - n)
        
        elif n <= 20:
            return max(missing, replace)
        
        else:
            delete = n - 20
            
            # Use deletions smartly
            use = min(delete, one)
            replace -= use
            delete -= use
            
            use = min(delete // 2, two)
            replace -= use
            delete -= use * 2
            
            replace -= delete // 3
            
            return (n - 20) + max(missing, replace)