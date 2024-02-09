        total = 0
        start = 0

        for end in range(len(fruits)):
            count[fruits[end]] += 1
            total += 1

            while len(count) > 2:
                count[fruits[start]] -= 1
                total -= 1

                if count[fruits[start]] == 0:
                    del count[fruits[start]]
        res = 0
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
class Solution:
[1,2,1]
