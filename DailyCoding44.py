# [2, 4, 1, 3, 5]
import collections
class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def bfs(root):
    q = collections.deque([])
    q.append(root)
    while q:
        s = len(q)
        for _ in range(s):
            c = q.popleft()
            print c.val,
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)
        print


def countTree(root):
    if not root:
        return 0
    leftTree = countTree(root.left)
    rightTree = countTree(root.right)
    return leftTree+rightTree+1

def insert(root,val):
    invert = 0
    if val > root.val:
        if not root.right:
            root.right = TreeNode(val)
        else:
            invert += insert(root.right,val)
    else:
        invert += countTree(root.right)
        invert +=1
        if not root.left:
            root.left = TreeNode(val)
        else:
            invert += insert(root.left,val)
    return invert

def createBinaryTree(nums):
    root = TreeNode(nums[0])
    re = 0
    for i in range(1,len(nums)):
        re += insert(root,nums[i])
    print re
    return root

root = createBinaryTree([5,4,3,2,1])
