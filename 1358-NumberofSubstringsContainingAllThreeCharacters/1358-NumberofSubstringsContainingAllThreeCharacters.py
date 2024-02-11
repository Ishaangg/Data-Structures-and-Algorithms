class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        for end in range(len(s)):
        res = 0
        start = 0

            dict_count[s[end]] += 1

            while (dict_count['a'] and dict_count['b'] and dict_count['c']):
                res += len(s) - end
                dict_count[s[start]] -= 1

                start += 1
        
        return res
        dict_count = collections.defaultdict(int)

"
