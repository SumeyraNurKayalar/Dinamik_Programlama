def min_total_time(n, m, time, cost):
    dp = [[float('inf')] * m for _ in range(n)]

    # İlk iş
    for j in range(m):
        dp[0][j] = time[0][j]

    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                dp[i][j] = min(dp[i][j], dp[i-1][k] + cost[k][j] + time[i][j])

    return min(dp[n-1])

n = 3
m = 2

time = [
    [4, 5],
    [6, 3],
    [7, 8]
]
cost = [
    [0, 2],
    [3, 0]
]
print(min_total_time(n, m, time, cost))
