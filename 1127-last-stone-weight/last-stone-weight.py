class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq.heapify(stones)
        new_stones = []
        heapq.heapify(new_stones)

        for stone in stones:
            heapq.heappush(new_stones, -stone)

        while len(new_stones) > 1:
            x = -heapq.heappop(new_stones)
            y = -heapq.heappop(new_stones)

            diff = x - y

            if diff:
                heapq.heappush(new_stones,-diff)

        if new_stones:
            return -new_stones[0]
        else:
            return 0


