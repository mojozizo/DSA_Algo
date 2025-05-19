class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
        
        pivot = l

        def binary_search(left:int,right:int) -> int:
            while left <= right:
                half = (left + right) // 2
                if nums[half] > target:
                    right = half - 1
                elif nums[half] == target:
                    return half
                else:
                    left = half+1
            
            return -1
        
        result = binary_search(0,pivot-1)
        if result != -1:
            return result

        return binary_search(pivot,len(nums)-1)