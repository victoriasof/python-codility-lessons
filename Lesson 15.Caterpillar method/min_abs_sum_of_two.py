"""
Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, 
for 0 <= P <= Q < N.

For example, the following array A:
  A[0] =  1
  A[1] =  4
  A[2] = -3

has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2).
The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2.
The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5.
The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (-3)| = 2.
The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8.
The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (-3)| = 1.
The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(-3) + (-3)| = 6.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, 
returns the minimal abs sum of two for any pair of indices in this array.

For example, given the following array A:
  A[0] =  1
  A[1] =  4
  A[2] = -3

the function should return 1, as explained above.

Given array A:
  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3

the function should return |(-8) + 5| = 3.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [-1,000,000,000..1,000,000,000].

"""

def solution(A):

    A.sort()
    back, front = 0, len(A) - 1
    min_abs_sum = abs(A[0] * 2)

    while back <= front:
        # These are three situations where we don't need to proceed because it won't get any better
        if A[back] > 0:
            # 1. First element (the smallest one) in the caterpillar is positive, which means all elements
            #    are positive. The smallest absolute sum for this caterpillar is if we sum this smallest
            #    element with itself. So there is no point in checking the others, just return either that
            #    sum or the current min_abs_sum.
            return min(min_abs_sum, A[back] * 2)

        if A[front] < 0:
            # 2. Last element (the biggest one) in the caterpillar is negative, which means all elements
            #    are negative. The smallest absolute sum for this caterpillar is if we sum this biggest
            #    (least negative) element with itself. So there is no point in checking the others,
            #    just return either that sum or the current min_abs_sum.
            return min(min_abs_sum, A[front] * (-2))

        if A[back] == 0 or A[front] == 0 or min_abs_sum == 0:
            # 3. If we ever get to the zero element or the min_abs_sum is zero, return zero.
            #    Nothing beats zero.
            return 0
        # This is the line where the min_abs_sum is updated - I'm checking the back and front of the
        # caterpillar and trying to lower my min_abs_sum.
        min_abs_sum = min(min_abs_sum, abs(A[back] + A[front]), abs(A[back] * 2), abs(A[front] * 2))
        # This is the part where I decide how to move from this position. If I'm having all positives
        # or all negatives or zero, I won't get to this line (as those are handled at the beginning of
        # the loop. So, I'm having the most positive number on the front, and the most negative number
        # on the back. I'll move from the more extreme one as I want to minimize the sum.
        if A[back] + A[front] < 0:
            back += 1
        else:
            front -= 1

    return min_abs_sum


A = [1, 4, -3]
print(solution(A))   


A = [-8, 4, 5, -10, 3]
print(solution(A))    

#https://codesays.com/2014/solution-to-min-abs-sum-of-two-by-codility/