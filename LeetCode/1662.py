from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(map(str, word1)) == "".join(map(str, word2))
word1 = list(input())
word2 = list(input())

sol = Solution()
print(sol.arrayStringsAreEqual(word1, word2))