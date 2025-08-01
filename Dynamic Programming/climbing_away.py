MOD = 10**9 + 7

def climbing_ways(n):
    if n == 0 or n == 1:
        return 1

    a, b = 1, 1  # ways(0) = 1, ways(1) = 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    return b

# Input
n = int(input())
print(climbing_ways(n))
