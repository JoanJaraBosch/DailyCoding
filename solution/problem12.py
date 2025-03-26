def count_ways_general(n, X):
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to stay at step 0

    for i in range(1, n + 1):
        dp[i] = sum(dp[i - step] for step in X if i - step >= 0)

    return dp[n]

if __name__ == "__main__":
    # Example Usage:
    print(count_ways_general(4, {1, 3, 5}))  # Output: 3 ([1,1,1,1], [1,3], [3,1])
    print(count_ways_general(10, {1, 3, 5})) # Output: 47