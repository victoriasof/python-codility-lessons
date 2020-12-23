"""
An array A consisting of N integers is given. 
A triplet (P, Q, R) is triangular if it is possible to build a triangle 
with sides of lengths A[P], A[Q] and A[R]. 
In other words, triplet (P, Q, R) is triangular if 0 <= P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12

There are four triangular triplets that can be constructed from elements of this array, 
namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

    def solution(A)

that, given an array A consisting of N integers, 
returns the number of triangular triplets in this array.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12

the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000];
        each element of array A is an integer within the range [1..1,000,000,000].

"""

def solution(A):

    n = len(A)
    result = 0
    A.sort()

    for first in xrange(n-2):
        third = first + 2

        for second in xrange(first+1, n-1):

            while third < n and A[first] + A[second] > A[third]:
                third += 1

            result += third - second - 1

    return result


A = [10, 2, 5, 1, 8, 12]
print(solution(A))

#https://codesays.com/2014/solution-to-count-triangles-by-codility/

