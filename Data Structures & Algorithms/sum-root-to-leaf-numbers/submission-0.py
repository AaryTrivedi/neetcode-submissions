# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        number = []
        numbers = []
        total = 0
        self.getNumbers(root, number, numbers)
        return sum(numbers)
    
    def getNumbers(self, root, num, numbers):
        if root is None:
            return
        num.append(root.val)
        self.getNumbers(root.left, num, numbers)
        if self.isLeaf(root):
            numFromArr = self.getIntFromNumsArray(num)
            numbers.append(numFromArr)
        self.getNumbers(root.right, num, numbers)
        num.pop(-1)
    
    def getIntFromNumsArray(self, arr):
        num = 0
        arrLen = len(arr) - 1
        for i in range(arrLen, -1, -1):
            num += arr[i] * (10 ** (arrLen - i))
        return num
    
    def isLeaf(self, root):
        return root.left is None and root.right is None