def findAnagrams( s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    dic = {}
    res = []
    for i in p:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    start, end, cnt = 0, 0, len(p)
    while end < len(s):
        if s[end] in dic:
            if dic[s[end]] >= 1:
                cnt -= 1
            dic[s[end]] -= 1
        end += 1
        if cnt == 0:
            res.append(start)
        if end - start == len(p):
            if s[start] in dic:
                if dic[s[start]] >= 0:
                    cnt += 1
                dic[s[start]] += 1
            start += 1
    return res

print findAnagrams("cbaebabacd","abc")