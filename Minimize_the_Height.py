class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[n-1] - arr[0]
        
        small = arr[0] + k
        big = arr[n-1] - k
        
        if small > big:
            small, big = big, small
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            
            mini = min(small, arr[i] - k)
            maxi = max(big, arr[i-1] + k)
            
            ans = min(ans, maxi - mini)
        
        return ans
