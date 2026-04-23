class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numCounter = {}

        for num in nums:
            if num in numCounter:
                numCounter[num] += 1
            else:
                numCounter[num] = 1
        
        largest = -1
        for key, value in numCounter.items():
            if value == 1 and key > largest:
                largest = key
        
        return largest