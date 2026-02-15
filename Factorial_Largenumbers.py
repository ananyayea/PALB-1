class Solution:
    def factorial(self, n):
        # Calculate factorial
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        
        # Convert factorial to list of digits
        return [int(d) for d in str(fact)]
