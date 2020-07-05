from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words):
        adjacent = defaultdict(set)
        counter = {}
        for word in words:
            for c in word:
                if c not in counter.keys():
                    counter[c] = 0

        for x in range(0,len(words)-1):
            first = words[x]
            second = words[x+1]
            if first.startswith(second):
                if len(second) < len(first):
                    return ""
            for x, y in zip(first, second):
                if x != y:
                    if y not in adjacent[x]:
                        adjacent[x].add(y)
                        counter[y] += 1
                    break

        output = []
        queue = deque([ a for a in counter if counter[a] == 0])

        while(queue):
            w = queue.popleft()
            output.append(w)
            for adj in adjacent[w]:
                counter[adj] -= 1
                if counter[adj] == 0:
                    queue.append(adj)

        if len(output) < len(counter):
            return ""

        return "".join(output)


if __name__ == '__main__':
    f = Solution()
    i = ["abc","ab"]
    print(f.alienOrder(i))