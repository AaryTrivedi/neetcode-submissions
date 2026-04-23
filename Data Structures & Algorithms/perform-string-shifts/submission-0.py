class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        splitS = list(s)
        
        for operation in shift:
            if operation[0] == 0:
                while operation[1] > 0:
                    firstCharacter = splitS.pop(0)
                    splitS.append(firstCharacter)
                    operation[1] -= 1
            else:
                while operation[1] > 0:
                    lastCharacter = splitS.pop(-1)
                    splitS.insert(0, lastCharacter)
                    operation[1] -= 1
        
        return ''.join(splitS)