class Solution:
    def confusingNumber(self, n: int) -> bool:
        original = n
        rotatedNum = 0
        validRotated = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        invalidRotated = set([2, 3, 4, 5, 7])

        while n > 0:
            num = n % 10
            if num in invalidRotated:
                return False
            rotatedNum *= 10
            rotatedNum += validRotated[num]
            n = n // 10
        
        return original != rotatedNum