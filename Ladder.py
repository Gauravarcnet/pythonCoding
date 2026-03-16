# You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

#         with your first step you can stand on rung 1 or 2,
#         if you are on rung K, you can move to rungs K + 1 or K + 2,
#         finally you have to stand on rung N.

# Your task is to count the number of different ways of climbing to the top of the ladder.

# For example, given N = 4, you have five different ways of climbing, ascending by:

#         1, 1, 1 and 1 rung,
#         1, 1 and 2 rungs,
#         1, 2 and 1 rung,
#         2, 1 and 1 rungs, and
#         2 and 2 rungs.

# Given N = 5, you have eight different ways of climbing, ascending by:

#         1, 1, 1, 1 and 1 rung,
#         1, 1, 1 and 2 rungs,
#         1, 1, 2 and 1 rung,
#         1, 2, 1 and 1 rung,
#         1, 2 and 2 rungs,
#         2, 1, 1 and 1 rungs,
#         2, 1 and 2 rungs, and
#         2, 2 and 1 rung.

# The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

# Write a function:

#     class Solution { public int[] solution(int[] A, int[] B); }

# that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

# For example, given L = 5 and:
#     A[0] = 4   B[0] = 3
#     A[1] = 4   B[1] = 2







def solution(A, B):
    L = len(A)

    maxA = max(A)
    maxB = max(B)

    mod = 2 ** maxB

    # Fibonacci precomputation
    fib = [0] * (maxA + 2)
    fib[1] = 1
    fib[2] = 2

    for i in range(3, maxA + 2):
        fib[i] = (fib[i-1] + fib[i-2]) % mod

    result = []

    for i in range(L):
        result.append(fib[A[i]] % (2 ** B[i]))

    return result
