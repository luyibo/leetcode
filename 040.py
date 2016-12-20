__author__ = 'user'
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dp(0,target,sorted(candidates),res,[])

        return res

    def dp(self,pos,k,List,res,path):
        for i in range(pos,len(List)):
            if i>pos and List[i] == List[i-1]:continue
            if List[i] >k:continue
            if List[i] == k:
                res.append(path+[List[i]])
            self.dp(i+1,k-List[i],List,res,path+[List[i]])


s = Solution()
print s.combinationSum2([10,1,2,7,6,1,5],8)