from typing import List

class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Reset result for multiple calls
        self.result = []
        # It is often helpful to sort, though not strictly required for this logic
        self.getCombinations([], 0, 0, nums, target)
        return self.result
    
    def getCombinations(self, combination, currSum, start, nums, target):
        # Base Case 1: Target reached
        if currSum == target:
            self.result.append(list(combination))
            return # Stop recursing here
        
        # Base Case 2: Exceeded target
        if currSum > target:
            return

        # Start loop from 'start' index to avoid duplicate sets (permutations)
        for i in range(start, len(nums)):
            num = nums[i]
            
            combination.append(num)
            # Pass i as the 'start' for the next call because we can reuse the same number
            self.getCombinations(combination, currSum + num, i, nums, target)
            
            # Backtrack
            combination.pop()