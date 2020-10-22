'''
In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
'''

class Solution:
    def numPairsDivisibleBy60(self, T):
        freq, res = [0] * 60, 0
        for t in T:  # count the freq
            freq[t % 60] += 1
        for i in range(31):  # check "0 - 30" (i-th)
            if (i == 0 or i == 30):  # e.g: 60, 180, 360, 720
                n = freq[i]
                res += n * (n - 1) // 2  # combination (pick two of them up)
            else:
                res += freq[i] * freq[60 - i]  # permutation
        return res

if __name__ == '__main__':
    f = Solution()
    print(f.numPairsDivisibleBy60([30,20,150,100,40]))