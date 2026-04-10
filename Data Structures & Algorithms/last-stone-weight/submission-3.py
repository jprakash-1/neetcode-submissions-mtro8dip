class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones)> 1: 
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            print(first, second, second - first)

            if second - first > 0:
                heapq.heappush(stones, first - second)
        
        return abs(stones[0]) if stones else 0