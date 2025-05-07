def maxKnights(n):
    if n == 1:
        return 1
    elif n == 2:
        return 4
    else:
        return (n * n + 1) // 2

# Test Case
n=int(input().strip())
print(maxKnights(n))  # Output: 4