//This Codility problem is called NumberSolitaire.
//It is solved using Dynamic Programming.

//I'll explain it step-by-step simply, then show the Python solution.
index:  0   1   2   3   4   5
A   =  [1, -2,  0,  9, -1, -2]



def solution(A):
    N = len(A)
    
    dp = [float('-inf')] * N
    dp[0] = A[0]

    for i in range(1, N):
        for dice in range(1, 7):
            if i - dice >= 0:
                dp[i] = max(dp[i], dp[i-dice] + A[i])

    return dp[N-1]
