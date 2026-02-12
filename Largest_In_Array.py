class Solution:
    def largest(self, arr):
        max_element = arr[0]
        
        for num in arr:
            if num > max_element:
                max_element = num
                
        return max_element
