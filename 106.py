# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder: return None
        root = TreeNode(postorder.pop())
        n = inorder.index(root.val)
        root.right = self.buildTree(inorder[n + 1:], postorder)
        root.left = self.buildTree(inorder[:n], postorder)
        return root
