# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))

    def checkBST(self, root, min, max):
        if root is None:
            return True

        if root.val>min and root.val<max:
            return self.checkBST(root.left, min, root.val) and self.checkBST(root.right, root.val, max)
        else:
            return False

        