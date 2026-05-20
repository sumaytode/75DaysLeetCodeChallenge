from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # remove punctuation and lowercase
        words = re.findall(r'\w+', paragraph.lower())

        count = Counter()

        for word in words:

            if word not in banned:
                count[word] += 1

        return max(count, key=count.get)