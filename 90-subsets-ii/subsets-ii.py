class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        sum_array = []
        def recursion(index,new_arr):

            if index >= n:
                if new_arr not in sum_array:
                    sum_array.append(new_arr[:])
                    return
            
            new_arr.append(nums[index])
            recursion(index+1, new_arr)

            new_arr.remove(nums[index])
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1
            recursion(index+1, new_arr)

        recursion(0,[])

        return sum_array


        