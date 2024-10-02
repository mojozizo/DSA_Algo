class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(candidates)
        final_arr = []
        def recursion(index,target, new_arr):

            if index >= n:
                if target == 0:
                    final_arr.append(new_arr[:])
                return
            
            if candidates[index] <= target:
                new_arr.append(candidates[index])
                recursion(index,target - candidates[index], new_arr)
                new_arr.pop()

            recursion(index+1,target, new_arr)

        recursion(0,target,[])

        return final_arr
        