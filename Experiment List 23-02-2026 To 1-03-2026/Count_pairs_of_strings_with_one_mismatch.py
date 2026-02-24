class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        
        pattern_count = defaultdict(int)
        total_pairs = 0
        
        for word in arr:
            for i in range(len(word)):
                # Create pattern by removing one character
                pattern = word[:i] + "*" + word[i+1:]
                
                # If pattern already exists, it forms valid pairs
                total_pairs += pattern_count[pattern]
                
                # Increase pattern frequency
                pattern_count[pattern] += 1
        
        return total_pairs
