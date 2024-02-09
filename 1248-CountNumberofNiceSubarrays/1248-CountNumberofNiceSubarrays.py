                    i += 1
            if temp == k:
                while(nums[i]%2 == 0):
                    count += 1

        while(j < len(nums)):

            if nums[j]%2 != 0:
                temp += 1
                count = 0
        temp = 0
        ans = 0
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        j = 0
[
