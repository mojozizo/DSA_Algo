class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxHeap = []
        # heapq.heapify(maxHeap)

        # for num in nums:
        #     heapq.heappush(maxHeap,-num)

        
        # return -maxHeap[k-1]

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]

        

        

