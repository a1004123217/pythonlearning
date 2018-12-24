class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = range(1, n+1)
        self.dfs(nums, k, [], res)
        return res
    def dfs(self,nums, k, path, res):
        if k == 0:
            res.append(path)
            return
        if len(nums) >= k:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], k-1, path+[nums[i]], res)
        return