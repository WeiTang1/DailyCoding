import collections
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.left.right = TreeNode("e")
root.right.left = TreeNode("f")

def printLevel(root):
    queue = collections.deque([root])
    while len(queue)>0:
        l = len(queue)
        for _ in range(l):
            node = queue.popleft()
            print node.val,
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print

printLevel(root)

def solution(root):
    if not root:
        return root
    root.left = solution(root.left)
    root.right = solution(root.right)
    root.left,root.right = root.right,root.left
    return root

solution(root)
printLevel(root)