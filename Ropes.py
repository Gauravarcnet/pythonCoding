# There are N ropes numbered from 0 to N − 1, whose lengths are given in an array A, lying on the floor in a line. For each I (0 ≤ I < N), the length of rope I on the line is A[I].

# We say that two ropes I and I + 1 are adjacent. Two adjacent ropes can be tied together with a knot, and the length of the tied rope is the sum of lengths of both ropes. The resulting new rope can then be tied again.

# For a given integer K, the goal is to tie the ropes in such a way that the number of ropes whose length is greater than or equal to K is maximal.

# For example, consider K = 4 and array A such that:
#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 1
#     A[5] = 1
#     A[6] = 3

# The ropes are shown in the figure below.

# We can tie:



def solution(K, A):
    count = 0
    current_length = 0

    for rope in A:
        current_length += rope

        if current_length >= K:
            count += 1
            current_length = 0

    return count

