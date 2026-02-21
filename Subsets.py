class Solution:
    def subsets(self, nums):
        result = []
        
        def backtrack(start, path):
            # Add current subset
            result.append(path[:])
            
            for i in range(start, len(nums)):
                # Choose
                path.append(nums[i])
                
                # Explore
                backtrack(i + 1, path)
                
                # Backtrack
                path.pop()
        
        backtrack(0, [])
        return result
