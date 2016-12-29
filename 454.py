def fourSumCount(A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    res = {}
    cnt = 0
    for i in range(len(A)):
            for j in range(len(B)):
                if A[i] + B[j] in res:
                    res[A[i] + B[j]] += 1
                else:
                    res[A[i] + B[j]] = 1
    for i in range(len(C)):
            for j in range(len(D)):
                if -(C[i] + D[j]) in res:
                    cnt += res[-(C[i] + D[j])]
    return cnt
import collections
def four(A,B,C,D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)

four([1,2]
,[-2,-1]
,[-1,2]
,[0,2])