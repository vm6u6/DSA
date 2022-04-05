class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def LCA( root, p, q ):
    if root is None:
        return None
            
    if root == p or root == q:
        return root
   
    rightLCA = LCA( root.right, p, q )
    leftLCA = LCA(root.left, p, q)
            
    if rightLCA and leftLCA is not None:
        return root
            
    if rightLCA is None:
        return leftLCA
    else:
        return rightLCA

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


p = TreeNode(5)
p.left = TreeNode(6)
p.right = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(0)
q.right = TreeNode(8)

print(LCA( root, p, q ))