'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0

Constraints:

-231 <= x <= 231 - 1
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0: return x
        rx = [i for i in str(x)]
        n = False
        if rx[0] == '-':
            n = True
            rx = rx[1:]

        rx.reverse()
        res = int(''.join(rx))
        if abs(res) > (2 ** 31 - 1): return 0
        if n: return res*-1
        else: return res


if __name__ == '__main__':
    f = Solution()
    print(f.reverse(120))
