            
            for i in range(start , len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                
                new_target = target - candidates[i]
                new_current = current + [candidates[i]] 
            
                solve(candidates, new_target, new_current, i+1, result)

        solve(candidates, target, [], 0, result)
                result.append(current)
                return result
            if target == 0:
        def solve(candidates, target, current,start, result):
        return result
[
