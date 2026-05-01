class Solution:

    def __init__(self):
        self.allSubsets = [[]]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            self.allSubsets.append([nums[i]])
            self.generateSubSets([nums[i]], i + 1, nums)

        return self.allSubsets
    
    def generateSubSets(self, currSubset, index, nums):
        for i in range(index, len(nums)):
            currSubset.append(nums[i])
            self.generateSubSets(currSubset, i + 1, nums)
            self.allSubsets.append(currSubset.copy())
            currSubset.pop(-1)