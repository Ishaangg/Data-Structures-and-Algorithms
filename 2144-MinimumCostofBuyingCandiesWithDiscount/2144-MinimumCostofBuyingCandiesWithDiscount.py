class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        cost.reverse()
        i = 0


        while i<N:
            ans += cost[i]
            if i+1 <N:
                ans += cost[i+1]
            i += 3
        return ans  
        N = len(cost)

[
