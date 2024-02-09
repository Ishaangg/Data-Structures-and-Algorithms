        start = 0

        for end in range(len(fruits)):
            count[fruits[end]] += 1
            total += 1

            while len(count) > 2:
                count[fruits[start]] -= 1
                total -= 1

                if count[fruits[start]] == 0:
                    del count[fruits[start]]

            res = max(total, res)
        return res
[
