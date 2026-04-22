class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightLarger = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > rightLarger:
                tmp = arr[i]
                arr[i] = rightLarger
                rightLarger = tmp
            else:
                arr[i] = rightLarger
        
        return arr