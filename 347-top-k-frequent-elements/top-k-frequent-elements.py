class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dictionary = {}
   
        for value in nums:
            
            if value not in dictionary:
                dictionary[value] = 1
            else:
                dictionary[value] += 1

        keys = sorted(dictionary.items(), key = lambda x: x[1], reverse=True)

        final_list = []
        for i in range(k):
            final_list.append(keys[i][0])

        return final_list
        
        