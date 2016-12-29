'''
题目的意思就是给出一个字符串，返回使用该字符串中字符组成的最长回文字符串的长度。
我的思路就是扫描一遍给出的字符串，统计每个字符出现的个数。然后遍历一遍各个字符的个数，
如果个数是偶数，则直接添加到长度中；如果个数是奇数，则添加个数-1到长度中并且标记存在中心字符，
因为只有偶数个字符才能分配到回文字符串的两端，而中心可以是单个字符，最后直接返回长度即可。
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        dic = {}
        hascenter = 0
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i]%2:
                length += dic[i]-1
                hascenter = 1
            else:
                length += dic[i]
        return length+hascenter