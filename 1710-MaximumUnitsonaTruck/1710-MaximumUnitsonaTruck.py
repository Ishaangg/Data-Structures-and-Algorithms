        boxTypes.sort(key = lambda x: x[1], reverse = True)
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
class Solution:
        ans = 0
        for box in boxTypes:
            x = min(box[0], truckSize)
            ans += (x*box[1])
            truckSize -= x
            if truckSize == 0:
                break
        return ans

[
