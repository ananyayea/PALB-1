class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        result = []

        while i < n1 and j < n2 and k < n3:
            
            # If elements are equal
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                current = arr1[i]
                
                # Skip duplicates in all arrays
                while i < n1 and arr1[i] == current:
                    i += 1
                while j < n2 and arr2[j] == current:
                    j += 1
                while k < n3 and arr3[k] == current:
                    k += 1

            # Move pointer of smallest element
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1

        return result if result else [-1]
