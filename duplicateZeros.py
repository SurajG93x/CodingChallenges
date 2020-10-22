'''
1089. Duplicate Zeros
Easy

491

197

Add to List

Share
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.



Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]


Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''

class Solution:
    def duplicateZeros(self, arr):
        dCheck = False
        n = len(arr)
        for i,num in enumerate (arr):
            if i < n-1 and num == 0:
                if not dCheck:
                    arr.insert(i+1,0)
                    arr.pop()
                    dCheck = True
                else:
                    dCheck = False
                    continue

        return arr

if __name__ == '__main__':
    f = Solution()
    print(f.duplicateZeros([1,0,2,3,0,4,5,0]))