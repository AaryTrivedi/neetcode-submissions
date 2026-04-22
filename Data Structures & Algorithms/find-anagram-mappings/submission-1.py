class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numIndexMap = {}
        
        for num in nums1:
            numIndexMap[num] = -1
        
        for i in range(len(nums2)):
            numIndexMap[nums2[i]] = i
        
        indices = []
        for num in nums1:
            indices.append(numIndexMap[num])
        
        return indices