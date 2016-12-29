def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    cnt = 0
    for i in range(len(points)):
        res = {}
        for j in range(len(points)):
            if i == j:
                continue
            dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if dis not in res:
                res[dis] = 0
            cnt += res[dis] * 2
            res[dis] += 1
        print res

    return cnt

numberOfBoomerangs([[0,0],[1,0],[2,0],[1,1]])