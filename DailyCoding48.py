
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def levelorder(root):
    stack = []
    stack.append(root)

    while stack:

        nextstack = []
        for node in stack:
            print node.val,
            if node.left:
                nextstack.append(node.left)
            if node.right:
                nextstack.append(node.right)
        print
        stack = nextstack

preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
def reconstruct(preorder, inorder):
    if preorder == []:
        return None

    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])

    leftpreorder = preorder[1:1+index]
    leftinorder = inorder[:index]
    root.left = reconstruct(leftpreorder,leftinorder)
    rightpreorder = preorder[index+1:]
    rightinorder = inorder[index+1:]
    root.right = reconstruct(rightpreorder,rightinorder)

    return root

root = reconstruct(preorder,inorder)

levelorder(root)