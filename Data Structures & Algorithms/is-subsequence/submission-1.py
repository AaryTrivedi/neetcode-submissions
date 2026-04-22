class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sI = 0
        sL = len(s)
        tI = 0
        tL = len(t)

        while sI < sL and tI < tL:
            if s[sI] == t[tI]:
                sI += 1
            tI += 1
        
        print(sI, sL, tI, tL)
        
        return sI == sL