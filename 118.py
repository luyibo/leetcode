def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0: return []
    basic = []
    for i in range(1, numRows+1):
        basic.append([1]*i)
        for j in range(2,i):
            basic[i-1][j-1] = basic[i-2][j-2]+basic[i-2][j-1]
    return basic

print generate(5)