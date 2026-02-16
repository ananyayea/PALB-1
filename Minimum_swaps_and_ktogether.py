class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: Count elements <= k
        good = sum(1 for x in arr if x <= k)
        
        # Step 2: Count bad elements in first window
        bad = sum(1 for x in arr[:good] if x > k)
        
        ans = bad
        left = 0
        
        # Step 3: Slide the window
        for right in range(good, n):
            
            # Remove left element
            if arr[left] > k:
                bad -= 1
            left += 1
            
            # Add right element
            if arr[right] > k:
                bad += 1
            
            ans = min(ans, bad)
        
        return ans
