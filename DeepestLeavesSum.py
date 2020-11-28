'''
Given a binary tree, return the sum of values of its deepest leaves.


Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''
class Solution:
    def deepestLeavesSum(self, root):
        currlvl = [root]

        while currlvl:
            nxt = []

            for node in currlvl:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)

            if not nxt:
                break

            currlvl = nxt

        return sum([node.val for node in currlvl])