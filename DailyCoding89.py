def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def helper(root, ceiling, floor):
        if not root:
            return True

        if root.val >= ceiling:
            return False
        if root.val <= floor:
            return False
        return helper(root.left, min(ceiling, root.val), floor) and helper(root.right, ceiling, max(floor, root.val))

    return helper(root, float("+inf"), float("-inf"))