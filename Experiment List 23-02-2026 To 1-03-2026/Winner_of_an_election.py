class Solution:
    def winner(self, arr):
        from collections import defaultdict
        
        vote_count = defaultdict(int)
        
        # Step 1: Count votes
        for name in arr:
            vote_count[name] += 1
        
        max_votes = 0
        winner_name = ""
        
        # Step 2: Find winner with tie-breaking
        for name in vote_count:
            if (vote_count[name] > max_votes or 
               (vote_count[name] == max_votes and name < winner_name)):
                
                max_votes = vote_count[name]
                winner_name = name
        
        return [winner_name, str(max_votes)]
