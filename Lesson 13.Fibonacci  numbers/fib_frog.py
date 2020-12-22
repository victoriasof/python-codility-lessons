"""

The Fibonacci sequence is defined using the following recursive formula:
    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2

A small frog wants to get to the other side of a river. 
The frog is initially located at one bank of the river ...
and wants to get to the other bank (position N). 

The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. 
Luckily, there are many leaves on the river, and the frog can jump between the leaves, 
but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. 
Consecutive elements of array A represent consecutive positions from 0 to ... on the river. 
Array A contains only 0s and/or 1s:

        0 represents a position without a leaf;
        1 represents a position containing a leaf.

The goal is to count the minimum number of jumps in which the frog can get to the other side 
of the river ...

The frog can jump between positions ... and N (the banks of the river) 
and every position containing a leaf.

For example, consider array A such that:
    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0

The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps 
by which the frog can get to the other side of the river. 
If the frog cannot reach the other side of the river, the function should return -1.

For example, given:
    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0

the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.

"""

import sys


def generate_fib_steps(n):
    a, b = 1, 1
    yield 1
    while a + b <= n:
        yield a + b
        a, b = b, a + b


def solution(A):
    n = len(A) + 1

    ret = [sys.maxsize] * (n + 1)
    ret[0] = 0

    for i in range(1, n + 1):
        if (i < n and A[i - 1] == 1) or (i == n):
            ret[i] = min([ret[i - x] + 1 for x in generate_fib_steps(i)])

    return ret[-1] if ret[-1] < sys.maxsize else -1


A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))

#https://medium.com/@thinh.onblurvn/fibfrog-from-codility-196037ed3e1a
