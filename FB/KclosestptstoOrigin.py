import math

class Solution:
    def kClosest(self, points, K):
        ed = lambda a, b : math.sqrt(a**2 + b**2)
        distlist = []
        res=[]

        for i,val in enumerate(points):
            distlist.append(ed(val[0],val[1]))

        list1 = ["a", "b", "c"]
        list2 = [2, 3, 1]

        zipped_lists = zip(list2, list1)

        sorted_zipped_lists = sorted(zipped_lists)
        sorted_list1 = [element for _, element in sorted_zipped_lists]

        sortedpts = [points for _, points in sorted(zip(distlist, points))]

        for j in range(0,K):
            res.append(sortedpts[j])

        return res

if __name__ == '__main__':
    f = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(f.kClosest(points,K))