class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        max_count = 0
        result = -1
        
        for i in range(n):
            # Binary search to find first occurrence of 1
            low, high = 0, m - 1
            first_one = -1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[i][mid] == 1:
                    first_one = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            if first_one != -1:
                count_ones = m - first_one
                if count_ones > max_count:
                    max_count = count_ones
                    result = i
        
        return result
