class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        res = 0

        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)


            while (end - start + 1) - max(count.values()) > k:
                start += 1
                count[s[start]] -= 1
            
            res = max(end - start + 1, res)
        return res
            
"
