class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(i):
            

            if i >= len(nums):
                return result.append(subset.copy())
        subset = []

            subset.append(nums[i])
            solve(i+1)
            subset.pop()

            solve(i+1)
        
        solve(0)
        return result
[
