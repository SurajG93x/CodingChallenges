class Solution:
    def test(self, debts):
        rows = debts[0]
        n = debts[1]
        debts = debts[2:]

        debtDict = {}

        dl = [debts[i:i+n] for i in range(0,len(debts),n)]

        for x in dl:
            borrow = x[0] #negate
            lend = x[1] #add

            if x[0] not in debtDict:
                debtDict[x[0]] = 0
            if x[1] not in debtDict:
                debtDict[x[1]] = 0

            debtDict[x[0]] -= x[2]
            debtDict[x[1]] += x[2]

        sd = {}
        for i in sorted(debtDict, key=debtDict.get):
            sd[i] = debtDict[i]

        res = []
        for n in sd:
            if sd[n] < 0:
                res.append(n)

        return res


if __name__ == '__main__':
    f = Solution()
    print(f.test([5,3,'Alex', 'Blake' ,5, 'Blake', 'Alex' ,3,'Casey', 'Alex', 7,'Casey', 'Alex', 4,'Casey', 'Alex', 2]))
