import math

class Solution:
    def kClosest(self, points, K):
        ed = lambda a, b : math.sqrt(a**2 + b**2)
        distlist = []
        res=[]

        for i,val in enumerate(points):
            distlist.append(ed(val[0],val[1]))

        sortedpts = [points for _, points in sorted(zip(distlist, points))]

        for j in range(0,K):
            res.append(sortedpts[j])

        return res

if __name__ == '__main__':
    f = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(f.kClosest(points,K))