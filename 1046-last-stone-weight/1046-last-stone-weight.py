class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]

        for  n in stones:
            heapq.heappush(heap,-n)

        while len(heap)>=2:
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
            heapq.heappush(heap,x-y)

        return -heap[0]