class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        candidates.sort()
        final_arr = []
        def recursion(index,new_arr, target):

            if target == 0:
                final_arr.append(new_arr[:])
                return
            
            for i in range(index,n):

                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break
            
                new_arr.append(candidates[i])
                recursion(i+1,new_arr, target-candidates[i])
                new_arr.pop()


        recursion(0,[], target)
        return final_arr