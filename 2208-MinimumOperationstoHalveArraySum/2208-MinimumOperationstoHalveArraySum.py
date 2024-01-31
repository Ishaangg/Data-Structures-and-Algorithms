import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sums = sum(nums)
        count = 0
        pq = [-num for num in nums]
        heapq.heapify(pq)
        current_sum = -sum(pq)
        while current_sum > sums/2:
            element = -heapq.heappop(pq)
            element = element / 2
            heapq.heappush(pq, -element)
            count += 1
            

        return count
            current_sum -= element

[
