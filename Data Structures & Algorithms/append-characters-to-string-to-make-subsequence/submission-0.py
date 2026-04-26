class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #.           a
        # s = thisisa
        # t = isagus
        #.       a

        if s == t:
            return 0

        sI = 0
        tI = 0

        while sI < len(s) and tI < len(t):
            if s[sI] == t[tI]:
                tI += 1
            sI += 1
        
        return len(t) - tI