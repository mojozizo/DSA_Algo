class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        s_nums = set(nums)
        res = []

        for i in range(1,len(nums)+1):
            if i not in s_nums:
                res.append(i)

        return res
        