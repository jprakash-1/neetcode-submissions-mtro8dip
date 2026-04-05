from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for start, end in intervals:
            # current interval completely before newInterval
            if end < newInterval[0]:
                res.append([start, end])

            # current interval completely after newInterval
            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end]

            # overlap
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        res.append(newInterval)
        return res