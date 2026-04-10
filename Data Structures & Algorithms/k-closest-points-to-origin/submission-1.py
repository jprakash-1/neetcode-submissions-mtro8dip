class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points: 
            dist = point[0]**2 + point[1]**2 
            minHeap.append((dist,point[0],point[1]))

        heapq.heapify(minHeap)
        res = []
        while k > 0: 
            dist, x, y = heapq.heappop(minHeap) 
            res.append((x,y))

            k -= 1 

        return res



        