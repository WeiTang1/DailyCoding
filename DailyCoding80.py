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
root.right.left = TreeNode("e")

def solution(root):
    if not root:
        return (-1,None)
    if not root.left and not root.right:
        return (0, root)
    leftlevel,leftdeep = solution(root.left)
    leftlevel+=1
    rightlevel, righedeep = solution(root.right)
    rightlevel+=1

    return (leftlevel,leftdeep) if leftlevel > rightlevel else (rightlevel,righedeep)



print solution(root)[1].val
def solution2(root):
    queue = collections.deque([root])
    lastqueue = queue
    while len(queue)>0:
        lastqueue = collections.deque(queue)
        l = len(queue)
        for _ in range(l):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return lastqueue

for node in  solution2(root):
    print node.val