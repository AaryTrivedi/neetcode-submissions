class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        wordIndexMap = {}

        for i in range(len(keyboard)):
            wordIndexMap[keyboard[i]] = i
        
        timeTaken = 0
        fingerPos = 0
        for i in range(len(word)):
            timeTaken += abs(fingerPos - wordIndexMap[word[i]])
            fingerPos = wordIndexMap[word[i]]
        
        return timeTaken