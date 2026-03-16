# For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

#     val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

# (Assume that the sum of zero elements equals zero.)

# For a given array A, we are looking for such a sequence S that minimizes val(A,S).

# Write a function:

#     def solution(A)

# that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

# For example, given array:
#   A[0] =  1
#   A[1] =  5
#   A[2] =  2
#   A[3] = -2


A = [abs(x) for x in A]
    total = sum(A)
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in A:
        for s in range(target, num-1, -1):
            if dp[s-num]:
                dp[s] = True

    for s in range(target, -1, -1):
        if dp[s]:
            return total - 2*s
