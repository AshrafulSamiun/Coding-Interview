import heapq
import sys

def median_stream(n, stream):
    max_heap = []  # lower half (max-heap simulated with negative values)
    min_heap = []  # upper half
    result = []

    for number in stream:
        if not max_heap or number <= -max_heap[0]:
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)

        # Rebalance
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        result.append(-max_heap[0])

    return result

# Input reading
n_and_stream = sys.stdin.read().split()
n = int(n_and_stream[0])
stream = list(map(int, n_and_stream[1:]))

medians = median_stream(n, stream)
for m in medians:
    print(m)
