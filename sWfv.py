import math

class Solution:
    def StringChallenge(self, strArr):
        p1 = strArr[0][1:len(strArr[0]) - 1]
        p2 = strArr[1][1:len(strArr[1]) - 1]
        p3 = strArr[2][1:len(strArr[2]) - 1]
        p4 = strArr[3][1:len(strArr[3]) - 1]

        p1 = tuple(map(int, p1.split(' ')))
        p2 = tuple(map(int, p2.split(' ')))
        p3 = tuple(map(int, p3.split(' ')))
        p4 = tuple(map(int, p4.split(' ')))

        l = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        b = math.sqrt((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2)
        print(int(l) * int(b))

if __name__ == '__main__':
    f = Solution()
    print(f.StringChallenge(['(1 1)', '(1 3)', '(3 1)', '(3 3)']))