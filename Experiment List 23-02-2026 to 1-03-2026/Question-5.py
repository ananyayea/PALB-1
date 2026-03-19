class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count frequency
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Step 2: Sort by (frequency, character)
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        # Step 3: Build result
        result = []
        for ch, count in sorted_chars:
            result.append(ch * count)
        
        return "".join(result)
