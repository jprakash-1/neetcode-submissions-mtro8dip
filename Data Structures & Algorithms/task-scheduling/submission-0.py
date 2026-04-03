from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-value for _, value in Counter(tasks).items()] 
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q: 
            time += 1 
            if maxHeap: 
                task = 1 + heapq.heappop(maxHeap)       
                if task:
                    q.append([task,time + n])
            if q and q[0][1] == time: 
                task = q.popleft()[0]
                heapq.heappush(maxHeap, task)
        return time

