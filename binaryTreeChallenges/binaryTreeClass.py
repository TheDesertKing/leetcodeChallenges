import random as r

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        r = '\n'+str(self.val)+'\n'
        c = [self.left,self.right]
        while c:
            r += '\t'.join([str(n.val) if n is not None else 'X' for n in c])+'\n'
            r = r.replace('\n','\n\t')
            c = sum([(n.left,n.right) for n in c if n is not None],())
        return r

node = TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(5)),TreeNode(12))
print(node)


