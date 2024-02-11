                seen.add(s)
            for j in range(i,n):
                if nums[j]%p == 0:
                    count += 1

                if count > k:
                    break 

                s += str(nums[j]) + "#"


        for i in range(n):
            s, count = "", 0
            
    def countDistinct(self, nums, k, p):
        n, seen = len(nums), set()

        return len(seen)

[
