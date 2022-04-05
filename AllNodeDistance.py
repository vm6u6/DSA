# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
#         def traval( root, k, ans ):
#             if root is None or k < 0:
#                 return ans
            
#             if k == 0:
#                 ans.append(root.val)
#                 return ans
            
#             traval( root.left, k-1, ans )
#             traval( root.right, k-1, ans )
        
#         def AllNodesDistance( root, target, k ):
#             ans = []
#             if root is None:
#                 visited = 0
#                 return ans, visited

#             if root == target:
#                 traval( root, k, ans)
#                 visited = 1
#                 return ans, visited

#             left, left_visited = AllNodesDistance( root.left, target, k )
#             right, right_visited = AllNodesDistance( root.right, target, k )
            

#             return ans
#         return AllNodesDistance( root, target, k )

def traval ( root, k, target, ans ):
    if root.left == target:
        if root.right == None or k<0:
            return ans
        if k == 0:
            ans.append(root.val)
            return ans
        traval( target, k-1, ans )
        traval( root.right, k-2, ans )

    return ans

def AllNodeDistance( root, k, target ):
    ans = []
    if root == None:
        return ans
    
    if root.right == target or root.left == target:
        traval( root, k, target, ans )

    left = AllNodeDistance(root.left, k, target)
    right = AllNodeDistance(root.right, k, target)

    return ans