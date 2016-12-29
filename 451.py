def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    res = {}
    temp = {}
    r = ''
    for c in s:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    for k, v in res.items():
        if v in temp:
            temp[v].append(k * v)
        else:
            temp[v] = [k * v]

    i = len(s)
    while i > 0:
        if i in temp:
            r += ''.join(temp[i])
        i -= 1
    return r

frequencySort('tree')