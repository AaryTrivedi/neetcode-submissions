class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIndex = -1
        
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] < target and matrix[mid][-1] >= target:
                rowIndex = mid
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                return True
        
        left, right = 0, len(matrix[rowIndex]) - 1
        while left <= right:
            mid = (left + right) // 2
            print(left, right, matrix[rowIndex][mid])

            if matrix[rowIndex][mid] < target:
                left = mid + 1
            elif matrix[rowIndex][mid] > target:
                right = mid - 1
            else:
                return True
        
        return False