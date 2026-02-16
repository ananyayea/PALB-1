class Solution:
    def spirallyTraverse(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        
        res = []
        
        while top <= bottom and left <= right:
            
            # Traverse top row
            for j in range(left, right + 1):
                res.append(mat[top][j])
            top += 1
            
            # Traverse right column
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1
            
            # Traverse bottom row (if still valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(mat[bottom][j])
                bottom -= 1
            
            # Traverse left column (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1
        
        return res
