class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        n = len(arr)
        i = 0

        # Initial sum will be of arr[0:k], i.e s = sum(arr[0:k])
        s = sum(arr[:k])
        avg = s / k

        # Total no of required subarrays
        res = 0

        while (True):
            # If current avg satisfies the condition
            if avg >= threshold:
                res += 1
            i += 1
            if i + k - 1 > n - 1:
                break

                # Remove the starting value and add one more value
            s = s - arr[i - 1] + arr[i + k - 1]
            avg = s / k
        return res


if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    f = Solution()
    print(f.numOfSubarrays(arr, k, threshold))