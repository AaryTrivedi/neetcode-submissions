class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wordIndexMap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in wordIndexMap:
                l = max(wordIndexMap[s[r]] + 1, l)
            wordIndexMap[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
