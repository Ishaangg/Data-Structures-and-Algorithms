            "T" : 0,
            "F" : 0
        }

        start = 0
        
        for end in range(len(answerKey)):
            count[answerKey[end]] += 1

            if (end - start + 1) - max(count.values()) > k:
                start += 1
        res = 0
                count[answerKey[start]] -= 1
            
            else:
        count = {
                res = max(res, end - start + 1)
        return res
"
