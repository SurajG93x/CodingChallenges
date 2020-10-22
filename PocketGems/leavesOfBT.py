'''
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []
[[3,5,4],[2],[1]], [[3,4,5],[2],[1]], etc, are also consider correct answers since per each level it doesn't matter the order on which elements are returned.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findLeaves(self, root):
        depthDict = defaultdict(list)
        self.dfs(depthDict, root)

        res = []
        for val in depthDict.values():
            res.append(val)

        return res

    def dfs(self, depthDict, root):
        if not root:
            return 0

        left = self.dfs(depthDict, root.left)
        right = self.dfs(depthDict, root.right)
        d = max(left, right) + 1
        depthDict[d].append(root.val)
        return d