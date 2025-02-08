#  LINK TO PROBLEM:
#  https://leetcode.com/problems/subtree-of-another-tree/

#  TAGS:
#  Trees

#  SOLUTION:
# We utilize a depth first search for this problem.
# We first check if the root and subroot are equal, if they are we then call our function on the subroot.left and subroot.right
# to compare them to root.left and root.right. This is done recurseively and if at any point they are not equal we return False
# If we get to the end of the tree and they are equal we return True

# TIME COMPLEXITY: O(n*m) - where n is the number of nodes in the main tree and m is the number of nodes in the sub tree
# SPACE COMPLEXITY: O(n+m) 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def solution(root: TreeNode, subRoot: TreeNode) -> bool:
    
    def dfsSub(root, subRoot):
                if not subRoot:
                    return not root
            
                if not root:
                    return False
                
                if root.val == subRoot.val:
                    return dfsSub(root.left, subRoot.left) and dfsSub(root.right,subRoot.right)
                
                else:
                    return False

    def dfsMain(root,subRoot):
        if not root:
              return False
        else:
            return dfsSub(root,subRoot) or dfsMain(root.right, subRoot) or dfsMain(root.left, subRoot)
         
    return dfsMain(root, subRoot)

#testing code
node1 = TreeNode(3)
node1.left = TreeNode(4)
node1.right = TreeNode(5)
node1.left.left = TreeNode(1)
node1.left.right = TreeNode(2)

node2 = TreeNode(4)
node2.left = TreeNode(1)
node2.right = TreeNode(2)

print(solution(node1,node2))
