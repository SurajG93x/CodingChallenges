'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        c = root.val
        while root:
            # update the closest value once the current note's value is more closet to target:
            if abs(root.val - target) < abs(c - target):
                c = root.val
            # use the binary search tree's property to find the closest value to target
            else:
                if root.val < target:
                    root = root.right
                else:
                    root = root.left
        return c