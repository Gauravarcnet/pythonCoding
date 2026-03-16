

# A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

# A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

# Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

# For example, consider an integer N = 26 and arrays P, Q such that:
#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20

# The number of semiprimes within each of these ranges is as follows:

#         (1, 26) is 10,
#         (4, 10) is 4,
#         (16, 20) is 0.

# Write a function:

#     class Solution { public int[] solution(int N, int[] P, int[] Q); }

# that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

# For example, given an integer N = 26 and arrays P, Q such that:
#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20

# the function should return the values [10, 4, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

#         N is an integer within the range [1..50,000];
#         M is an integer within the range [1..30,000];
#         each element of arrays P and Q is an integer within the range [1..N];
#         P[i] ≤ Q[i].









def solution(N, P, Q):
    # Step 1: smallest prime factor
    spf = [0] * (N + 1)

    i = 2
    while i * i <= N:
        if spf[i] == 0:
            j = i * i
            while j <= N:
                if spf[j] == 0:
                    spf[j] = i
                j += i
        i += 1

    # Step 2: identify semiprimes
    semiprime = [0] * (N + 1)

    for i in range(2, N + 1):
        if spf[i] != 0:
            p = spf[i]
            q = i // p
            if spf[q] == 0:
                semiprime[i] = 1

    # Step 3: prefix sum
    prefix = [0] * (N + 1)

    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + semiprime[i]

    # Step 4: answer queries
    result = []
    for p, q in zip(P, Q):
        result.append(prefix[q] - prefix[p - 1])

    return result

