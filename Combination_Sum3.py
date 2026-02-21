class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, path, remaining):
            # Base case
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Choose the number
                path.append(candidates[i])
                
                # Reuse same element (so pass i, not i+1)
                backtrack(i, path, remaining - candidates[i])
                
                # Backtrack (undo choice)
                path.pop()
        
        backtrack(0, [], target)
        return result
