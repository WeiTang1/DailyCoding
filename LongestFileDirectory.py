
import re
class Node:
    def __init__(self,val):
        self.val = val
        self.child=[]
        self.file = False
        self.currentPath = ""

    def addChild(self,child):
        self.child.append(child)
        if isFile(child.val):
            child.file = True;
        child.currentPath += child.val.strip() + '/'


dirstring = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print dirstring.split('\n');

def match(str,level):
    reg = r"" + level+"([a-z1-9]+)" + r""
    found = re.match(reg, str)
    if found:
        return True
    return False

def isFile(str):
    found = re.search(r"\w+\.\w+", str)
    if found:
        return True
    return False


def build(arr, level,path):
    if not arr:
        return None
    root = Node(arr[0])
    arr.remove(root.val)
    path += root.val.strip()+'/'
    root.currentPath = path;
    level = level +'\t'
    while(len(arr)!=0 and match(arr[0],level) is True):
        root.addChild(build(arr,level,path))
    return root


def DFS(root,str,maxlength):
    if not root:
        return ""
    if root.file:
        print root.currentPath
        str = str + root.val.strip()
        maxlength = max(len(str),maxlength)
    str += root.val.strip()+'/'
    for child in root.child:
        DFS(child,str,maxlength)
    return maxlength
