class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sorted_nums = sorted(nums)
        HashMap = {}

        for i in range(len(nums)):
            if sorted_nums[i] not in HashMap:
                HashMap[sorted_nums[i]] = i
        
        res = []
        for i in range(len(nums)):
            res.append(HashMap[nums[i]])

        
        return res