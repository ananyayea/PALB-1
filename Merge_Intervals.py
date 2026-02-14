class Solution:
    def merge(self, intervals):
        intervals.sort()  # sort by start time
        
        merged = []
        current = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= current[1]:
                # overlap → merge
                current[1] = max(current[1], intervals[i][1])
            else:
                merged.append(current)
                current = intervals[i]

        merged.append(current)
        return merged
