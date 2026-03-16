# A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

# For example, consider array A such that:
#   A[0] = -5
#   A[1] = -3
#   A[2] = -1
#   A[3] =  0
#   A[4] =  3
#   A[5] =  6

# The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

# Write a function:

#     class Solution { public int solution(int[] A); }

# that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

# For example, given array A such that:
#   A[0] = -5
#   A[1] = -3
#   A[2] = -1
#   A[3] =  0
#   A[4] =  3
#   A[5] =  6

# the function should return 5, as explained above.


def solution(A):
    left = 0
    right = len(A) - 1
    count = 0
    last = None

    while left <= right:
        left_val = abs(A[left])
        right_val = abs(A[right])

        if left_val > right_val:
            val = left_val
            left += 1
        elif left_val < right_val:
            val = right_val
            right -= 1
        else:
            val = left_val
            left += 1
            right -= 1

        if val != last:
            count += 1
            last = val

    return count
