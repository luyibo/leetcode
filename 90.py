class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:return None
        else:
            result = []
            result.append([])
            self.dfs(sorted(nums),0,[],result)
            return result
    def dfs(self,list,pos,path,result):
        for i in range(pos,len(list)):
            if i!=pos and list[i]==list[i-1]:
                continue
            else:
                result.append(path+[list[i]])
            self.dfs(list,i+1,path+[list[i]],result)

s = Solution()
print s.subsetsWithDup([1,2,2])