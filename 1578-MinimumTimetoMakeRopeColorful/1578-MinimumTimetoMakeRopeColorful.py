        while i < n:
            sum_val = 0
            mx = float('-inf')
            j = i

            while j < n and colors[i] == colors[j]:
                sum_val += neededTime[j]
                mx = max(mx, neededTime[j])
                j += 1

            ans += (sum_val - mx)
        i = 0
        ans = 0
        n = len(colors)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
            i·=·j

        return ans

"
