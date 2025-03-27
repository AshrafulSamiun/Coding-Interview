import sys
import bisect

# Read input
n = int(input().strip())
arr = list(map(int, input().split()))
k = int(input().strip())
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Step 1: Sort the array
arr.sort()

# Step 2: Answer each query using binary search
results = []
for l, r in queries:
    left_index = bisect.bisect_left(arr, l)  # First position >= l
    right_index = bisect.bisect_right(arr, r)  # First position > r
    results.append(right_index - left_index)

# Print all results
print("\n".join(map(str, results)) + "\n")