__author__ = 'lyb-mac'

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (q.val <= root.val <= p.val or q.val >= root.val >= p.val):
            return root.val
        if (q.val < root.val and p.val < root.val):
            return self.lowestCommonAncestor(root.left,p,q)
        if (q.val > root.val and p.val > root.val):
            return self.lowestCommonAncestor(root.right,p,q)