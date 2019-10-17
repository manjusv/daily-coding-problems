# There exists a staircase with N steps, and you can climb up
# either 1 or 2 steps at a time. Given N, write a function that
# returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
# For example, if N is 4, and set X = {1, 2} then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# This can be solved using dynamic programming
# time complexity - O(N * |X|)
# space complexity - O(N)


def staircase(N, X):
    dp = [0 for _ in range(N + 1)]

    # initialize dp[0] to 1 as base condition
    dp[0] = 1

    for i in range(1, N + 1):
        dp[i] += sum(dp[i - x] for x in X if i - x >= 0)

    return dp[N]


N = 4
X = (1, 2)
print(staircase(N, X))
