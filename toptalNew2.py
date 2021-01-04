'''
You want to spend your next vacation in a foreign country. In the summer you are free for N consecutive days. You have consulted Travel Agency and learned that they are offering a trip to some interesting location in the country every day. For simplicity, each location is identified by a number from 0 to N − 1. Trips are described in a non-empty array A: for each K (0 ≤ K < N), A[K] is the identifier of a location which is the destination of a trip offered on day K. Travel Agency does not have to offer trips to all locations, and can offer more than one trip to some locations.

You want to go on a trip every day during your vacation. Moreover, you want to visit all locations offered by Travel Agency. You may visit the same location more than once, but you want to minimize duplicate visits. The goal is to find the shortest vacation (a range of consecutive days) that will allow you to visit all the locations offered by Travel Agency.

For example, consider array A such that:

A[0] = 7
A[1] = 3
A[2] = 7
A[3] = 3
A[4] = 1
A[5] = 3
A[6] = 4
A[7] = 1
Travel Agency offers trips to four different locations (identified by numbers 1, 3, 4 and 7). The shortest vacation starting on day 0 that allows you to visit all these locations ends on day 6 (thus is seven days long). However, a shorter vacation of five days (starting on day 2 and ending on day 6) also permits you to visit all locations. On every vacation shorter than five days, you will have to miss at least one location.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the length of the shortest vacation that allows you to visit all the offered locations.

For example, given array A shown above, the function should return 5, as explained above.

Given A = [2, 1, 1, 3, 2, 1, 1, 3], the function should return 3. One of the shortest vacations that visits all the places starts on day 3 (counting from 0) and lasts for 3 days.

Given A = [7, 5, 2, 7, 2, 7, 4, 7], the function should return 6. The shortest vacation that visits all the places starts on day 1 (counting from 0) and lasts for 6 days.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..N − 1].
'''

class Solution:
    def solve(self, A):
        char_frequency = {}
        unique = len(set(A))
        left_pointer = 0
        min_length = float('inf')

        for right_pointer in range(len(A)):
            right_pointer_value = A[right_pointer]

            if right_pointer_value not in char_frequency:
                char_frequency[right_pointer_value] = 0

            char_frequency[right_pointer_value] += 1

            while len(char_frequency) == unique:
                left_pointer_value = A[left_pointer]

                min_length = min(min_length, right_pointer - left_pointer + 1)

                char_frequency[left_pointer_value] -= 1

                if char_frequency[left_pointer_value] == 0:
                    del char_frequency[left_pointer_value]

                left_pointer += 1

        return min_length


if __name__ == '__main__':
    f = Solution()
    print(f.solve([2, 1, 1, 3, 2, 1, 1, 3]))