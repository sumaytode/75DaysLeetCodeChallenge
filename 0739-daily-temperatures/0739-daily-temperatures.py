class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # store indices

        for i in range(n - 1, -1, -1):
            # Remove all smaller or equal temperatures
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            # If no greater temperature
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1] - i

            # Push current index
            stack.append(i)

        return result