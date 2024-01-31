        return remaining_sum
            element = -heapq.heappop(pq)
            element = element - element // 2
            heapq.heappush(pq, -element)
        remaining_sum = -sum(pq)
        while k:

import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-pile for pile in piles]
        heapq.heapify(pq)


            k -= 1

[
