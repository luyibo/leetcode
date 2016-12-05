class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return
        result = []
        result.append([])
        self.dfs(sorted(nums), result, 0, [])
        return result

    def dfs(self, List, result, pos, path):
        for i in range(pos, len(List)):
            result.append(path + [List[i]])
            self.dfs(List, result, i + 1, path + [List[i]])

s = Solution()
print s.subsets([1,2,4])