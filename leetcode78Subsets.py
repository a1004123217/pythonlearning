class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        sorted(nums)
        for num in nums:
            result += [i + [num] for i in result]
        return result
    def subsets2(self, nums):
        result = [[]]
        self.dfs(sorted(nums, 0, [], result))


    def dfs(self, nums, index, path, result):
        result.append(path)
        for i in range(nums):
            self.dfs(nums, i+1, path+[nums[i], result])