def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def helper(node):
        if not node:
            return 0
        leftbranch = helper(node.left)
        rightbranch = helper(node.right)
        self.max = max(self.max, node.val + leftbranch + rightbranch)
        return max(node.val + max(leftbranch, rightbranch), 0)

    self.max = None
    helper(root)
    return self.max