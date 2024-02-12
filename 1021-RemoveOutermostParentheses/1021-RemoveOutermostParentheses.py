class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        for c in s:
            if c == "(" and opened > 0: res.append(c)
        res, opened = [], 0
            if c == ")" and opened > 1: res.append(c)


            opened += 1 if c == "(" else -1
        
        return "".join(res)
        
"
