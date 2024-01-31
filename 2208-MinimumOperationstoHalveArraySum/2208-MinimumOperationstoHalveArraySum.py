        count = 0

        while removed < total_sum / 2:
            count += 1
            element = -heapq.heappop(pq) 
            element /= 2  
            removed += element
            heapq.heappush(pq, -element)  

        removed = 0
        heapq.heapify(pq)
        pq = [-num for num in nums]  
        total_sum = sum(nums)
    def halveArray(self, nums):
        return count

class Solution:


[
