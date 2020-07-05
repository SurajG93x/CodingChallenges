'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        resultLevels = []
        nextLevel = deque([root])

        while root and nextLevel:
            curr = nextLevel
            nextLevel = deque()
            resultLevels.append([])

            for root in curr:
                resultLevels[-1].append(root.val)

                if root.left:
                    nextLevel.append(root.left)
                if root.right:
                    nextLevel.append(root.right)

        return reversed(resultLevels)