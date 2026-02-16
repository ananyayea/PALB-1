class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        # Sorting is mandatory to handle duplicates and for pruning
        candidates.sort()

        def backtrack(remain, combo, start):
            if remain == 0:
                results.append(list(combo))
                return
            
            for i in range(start, len(candidates)):
                # If the current number is greater than the remaining target, 
                # no need to check further (pruning)
                if candidates[i] > remain:
                    break
                
                # Skip duplicate numbers at the same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                combo.append(candidates[i])
                # Move to i + 1 because each number can only be used once
                backtrack(remain - candidates[i], combo, i + 1)
                combo.pop()

        backtrack(target, [], 0)
        return results
