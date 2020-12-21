"""
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that ..., is called a double slice.
...

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
      ...
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, 
returns the maximal sum of any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        ...

"""

"""
#FIRST SOLUTION 

import sys

def solution(A):
    
    n = len(A)
    left = [0] * n

    for i in range(1, n-1):
        left[i] = max(0, left[i-1] + A[i])

    right = [0] * n 

    for i in range(n-2, 1, -1):
        right[i] = max(0, right[i+1] + A[i])

    max_sum = -sys.maxint

    for i in range(1, n-1):
        max_sum = max(max_sum, left[i-1] + right[i+1])

    return max_sum    

    #https://www.geeksforgeeks.org/sys-maxint-in-python/
"""

#SECOND SOLUTION:

def solution(A):

    N = len(A)

    A1 = [0]*N
    A2 = [0]*N

    maxCurrent = 0
    maxTotal = 0

    for i in range(1, N-1):
        A1[i] = maxCurrent = max(0, maxCurrent + A[i])

    maxCurrent = 0

    for i in range(N-2, 0, -1):
        A2[i] = maxCurrent = max(0, maxCurrent + A[i])

    for i in range(1, N-1):
        maxTotal = max(maxTotal, A1[i-1] + A2[i+1])

    return maxTotal

A = [3, 2, 6, -1, 4, 5, -1, 2]
print(solution(A))  

#https://codesays.com/2014/solution-to-max-double-slice-sum-by-codility/


