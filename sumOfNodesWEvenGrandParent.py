'''
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.



Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root) -> int:
        if not root:
            return 0

        total = 0
        level = [root]

        while level:
            curr = level.pop()

            if curr:
                level += [curr.left, curr.right]
                if curr.val % 2 == 0:
                    if curr.left:
                        if curr.left.left:
                            total += curr.left.left.val
                        if curr.left.right:
                            total += curr.left.right.val

                    if curr.right:
                        if curr.right.left:
                            total += curr.right.left.val
                        if curr.right.right:
                            total += curr.right.right.val

        return total