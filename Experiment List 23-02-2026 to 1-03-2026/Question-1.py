class Solution:
    def minSwaps(self, s1: str, s2: str) -> int:
        total_ones = s1.count('1') + s2.count('1')
        
        # If odd → impossible
        if total_ones % 2 != 0:
            return -1
        
        mismatch = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch += 1
        
        return mismatch // 2
