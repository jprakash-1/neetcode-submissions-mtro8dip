from _heapq import heappush
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr): 
            return arr 

        res = []
        for num in arr:
            dist = abs(num - x)
            heappush(res,[dist, num])

        ans = []

        for _ in range(k):
            dist, num = heapq.heappop(res)
            ans.append(num)

        ans.sort()


        return ans
