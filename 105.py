class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:return None
        root = TreeNode(preorder.pop(0))
        treeindex = inorder.index(root.val)
        root.left = self.buildTree(preorder,inorder[:treeindex])
        root.right = self.buildTree(preorder,inorder[treeindex+1:])
        return root