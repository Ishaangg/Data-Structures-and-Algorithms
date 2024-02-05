        def solve(candidates, result, target, sums, current):

            if sums == target:
                result.append(current)
                return result
            
            for i,element in enumerate(candidates):
                if element <= target - sums :

                    new_sums = sums + element
                    new_current = current + [element]

                    solve(candidates[i:], result, target, new_sums, new_current)
                
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        solve(candidates, result, target, 0, [])
        return result
[
