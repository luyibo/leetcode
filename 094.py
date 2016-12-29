class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if root == None:
            return
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)
