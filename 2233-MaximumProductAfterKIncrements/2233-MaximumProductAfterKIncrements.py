import heapq
    def maximumProduct(self, nums: List[int], k: int) -> int:
        modulo = 10**9 + 7
        mult = 1
class Solution:
        heapq.heapify(nums)
            element = heapq.heappop(nums)
        while k:

            element += 1
            heapq.heappush(nums,element)
        for num in nums:

        return mult 
             
           
            k -= 1
            mult = (mult*num) % modulo
[
