class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = []

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        while i < m:
            arr.append(nums1[i])
            i += 1
        
        while j < n:
            arr.append(nums2[j])
            j += 1
        
        for i in range(len(nums1)):
            nums1[i] = arr[i]