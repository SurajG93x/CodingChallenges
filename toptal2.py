import math
from collections import defaultdict

def solution(S, X, Y):
    hyp = lambda a, b: math.sqrt(a ** 2 + b ** 2)
    pointDict = {}

    n = len(S)
    flag = False
    single = False
    r = float('-inf')

    for i in range(0, n):
        if S[i] in pointDict:
            if hyp(pointDict[S[i]][0],pointDict[S[i]][1]) > hyp(X[i],Y[i]):
                pointDict[S[i]] = [X[i], Y[i]]
                flag = True
            elif hyp(pointDict[S[i]][0],pointDict[S[i]][1]) > hyp(X[i],Y[i]) and len(pointDict) == 1:
                single = True
            r = min(hyp(pointDict[S[i]][0],pointDict[S[i]][1]), hyp(X[i],Y[i]))
        else:
            pointDict[S[i]] = [X[i],Y[i]]
            if flag == False:
                r = max(r, hyp(X[i],Y[i]))



    res = 0
    if len(pointDict) == 1 and single == True:
        return 0

    for p in pointDict:
        if hyp(pointDict[p][0],pointDict[p][1]) >= r:
            res+=1

    return res

print(solution('CCD', [1, -1, 2], [1, -1, -2]))