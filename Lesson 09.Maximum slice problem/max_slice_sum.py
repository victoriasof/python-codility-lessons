"""
A non-empty array A consisting of N integers is given. 
...

Write a function:

    def solution(A)

that, given an array A consisting of N integers, 
returns the maximum sum of any slice of A.

For example, given array A such that:
A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0

the function should return 5 because:

        (3, 4) is a slice of A that has sum 4,
        ...
        no other slice of A has sum greater than (0, 1).

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..1,000,000];
        ...

"""

def solution(A):

        max_slice = 0
        result = A[0]

        for value in A:
                max_slice = max(value, max_slice + value)
                result = max(result, max_slice)

        return result 


A = [3, 2, -6, 4, 0]
print(solution(A))                

#https://codesays.com/2014/solution-to-max-slice-sum-by-codility/