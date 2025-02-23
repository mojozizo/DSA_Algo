class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # full_list = set(range(0,len(nums)+1))

        # for i in range(len(nums)):
        #     if nums[i] in full_list:
        #         full_list.remove(nums[i])
         
        # ans = full_list.pop()
        # return ans

        return sum(range(0,len(nums)+1)) - sum(nums)