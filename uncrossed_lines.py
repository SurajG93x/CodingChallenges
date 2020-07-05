'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
'''
class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        count = 0
        visitedA = []
        visitedB = []

        for i in range(0,min(len(A),len(B))):
            if A[i] == B[i]:
                count += 1
                visitedA.append(A[i])
                visitedB.append(B[i])

        countA = count
        countB = count

        for i in range(0, len(A)):
            for j in range(0,len(B)):
                va = []
                vb = []
                if i not in visitedA and j not in visitedA and j not in visitedB and i not in visitedB and A[i] == B[j] and i > j:
                    countA += 1
                    visitedA.append(i)
                    visitedB.append(j)

        for i in range(0, len(B)):
            for j in range(0,len(A)):
                if i not in visitedA and j not in visitedA and j not in visitedB and i not in visitedB and A[i] == B[j] and j > i:
                    countB += 1
                    visitedA.append(i)
                    visitedB.append(j)

        return max(countA,countB)

if __name__ == '__main__':
    f = Solution()
    z = f.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2])
    print(z)
