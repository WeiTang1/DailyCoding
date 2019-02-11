import collections
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)


def verticalView(root):
    q = collections.deque([(root,0)])
    hm = collections.defaultdict(list)
    while len(q)>0:
        node, level = q.popleft()
        if node:
            hm[level].append(node.val)
            q.append((node.left, level -1))
            q.append((node.right,level+1))

    return [hm[i][0] for i in sorted(hm.keys())]

print verticalView(root)