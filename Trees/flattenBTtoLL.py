'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatree(root)

    def flatree(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root

        leftTail = self.flatree(root.left)
        rightTail = self.flatree(root.right)

        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        if rightTail:
            return rightTail
        else:
            return leftTail