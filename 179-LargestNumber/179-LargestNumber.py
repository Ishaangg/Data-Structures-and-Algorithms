    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=LargerNumKey)
class Solution:


        largest_num = ''.join(nums)

    def __lt__(x, y):
class LargerNumKey(str):
        return x+y > y+x 
        return "0" if largest_num[0] == "0" else largest_num



        
                
[
