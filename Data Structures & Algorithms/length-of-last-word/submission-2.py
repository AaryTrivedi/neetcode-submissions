class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        right = len(s) - 1
        while s[right] == " ":
            right -= 1
        
        left = 0
        start = left
        while left < right:
            if s[left] == " " and s[left + 1].isalpha():
                start = left
            left += 1
        
        print (right, start)
        return right - start