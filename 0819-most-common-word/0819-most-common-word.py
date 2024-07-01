import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub("[^\w]", " ", paragraph).lower().split() if word not in banned]
        word_counter = Counter(words)

        return word_counter.most_common(1)[0][0]
