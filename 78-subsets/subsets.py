class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def recursion(index,new_arr):

            if index >= len(nums):
                subset.append(new_arr[:])
                return

            new_arr.append(nums[index])
            recursion(index+1,new_arr)

            new_arr.remove(nums[index])
            recursion(index+1,new_arr)

        recursion(0,[])

        return subset