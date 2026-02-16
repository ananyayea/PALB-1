class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        
        # Sorting helps us "prune" (stop early) the search tree
        candidates.sort()

        def backtrack(remain, combo, start):
            if remain == 0:
                # We found a valid combination
                results.append(list(combo))
                return

            for i in range(start, len(candidates)):
                # Optimization: If the current number is already greater than 
                # what's left, no point checking numbers after it (since it's sorted)
                if candidates[i] > remain:
                    break

                # Add the number and move deeper into the tree
                combo.append(candidates[i])
                
                # We pass 'i' as the start index to allow reusing the same number
                backtrack(remain - candidates[i], combo, i)
                
                # "Backtrack" by removing the last added number
                combo.pop()

        backtrack(target, [], 0)
        return results
