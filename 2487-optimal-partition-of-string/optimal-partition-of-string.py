class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        partitions = 1  
        seen = set()  
        
        for char in s:
            if char in seen:
                partitions += 1
                seen.clear()  
            
            seen.add(char) 
        
        return partitions
        
        