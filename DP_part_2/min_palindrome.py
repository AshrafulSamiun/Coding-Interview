def min_palindrome_cuts(s):
    n = len(s)
    
    # Step 1: Precompute all palindromes
    is_palindrome = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_palindrome[i][i] = True  # single char is palindrome

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True

    # Step 2: DP for min cuts
    dp = [0] * n
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0  # no cut needed
        else:
            dp[i] = float('inf')
            for j in range(i):
                if is_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]
