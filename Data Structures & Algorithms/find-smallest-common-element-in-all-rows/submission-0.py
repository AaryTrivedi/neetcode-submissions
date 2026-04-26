class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        min_set = set(mat[0])

        for row in mat[1:]:
            row_set = set(row)
            min_set = set([x for x in min_set if x in row_set])
        
        if len(min_set) > 0:
            return min(min_set)
        
        return -1