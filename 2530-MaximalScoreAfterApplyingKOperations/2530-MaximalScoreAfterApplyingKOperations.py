from math import ceil
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums]

        for i in range(k):
            element = -heapq.heappop(pq)

        heapq.heapify(pq)
            element = ceil(element//3) + 1
        score = []
            score.append(element)

        remaining_sum = sum(score)
            heapq.heappush(pq, -element)

        return remaining_sum

[
