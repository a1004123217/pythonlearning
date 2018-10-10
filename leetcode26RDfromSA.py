class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tnum = sorted(nums)
        #print(tnum)
        #print(len(nums))
        if len(nums) <= 1:
            return (nums)
        else:
            rst = [tnum[0],]
            tmp = tnum[0]
            for i in range(len(nums)):
                if tnum[i] != tmp:
                    rst.append(tnum[i])
                    #print('%s  %s\n'%(tnum[i] , rst))
                    tmp = tnum[i]
            for i in range(len(rst)):
                rst[i] = int(rst[i])
       # print(rst)
        return len(rst)
#[0,0,1,1,1,2,2,3,3,4]
test = Solution()
while True:
    x = input()
    xlist = x.split(',')
    #print(xlist)
    print(test.removeDuplicates(xlist))
