"""

You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. 
With each step, you can ascend by one or two rungs. More precisely:

        with your first step you can stand on rung 1 or 2,
        if you are on rung K, you can move to rungs K + 1 or K + 2,
        finally you have to stand on rung N.

Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

        1, 1, 1 and 1 rung,
        1, 1 and 2 rungs,
        1, 2 and 1 rung,
        2, 1 and 1 rungs, and
        2 and 2 rungs.

Given N = 5, you have eight different ways of climbing, ascending by:

        1, 1, 1, 1 and 1 rung,
        1, 1, 1 and 2 rungs,
        1, 1, 2 and 1 rung,
        1, 2, 1 and 1 rung,
        1, 2 and 2 rungs,
        2, 1, 1 and 1 rungs,
        2, 1 and 2 rungs, and
        2, 2 and 1 rung.

The number of different ways can be very large, so it is sufficient to return the result 
modulo 2P, for a given integer P.

Write a function:

    def solution(A, B)

that, given two non-empty arrays A and B of L integers, 
returns an array consisting of L integers specifying the consecutive answers; 
position I should contain the number of different ways of climbing the ladder 
with A[I] rungs modulo 2B[I].

For example, given L = 5 and:
    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1

the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        L is an integer within the range [1..50,000];
        each element of array A is an integer within the range [1..L];
        each element of array B is an integer within the range [1..30].

"""

def solution(A, B):

    limit    = max(A)                 # The possible largest N rungs
    result   = [0] * len(A)           # The result for each query
    modLimit = (1 << max(B)) - 1      # To avoid big interger in fibs

    # Compute the Fibonacci numbers for later use
    fib    = [0] * (limit+2)
    fib[1] = 1

    for i in xrange(2, limit + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) & modLimit

    for i in xrange(len(A)):
        # To climb to A[i] rungs, you could either
        # come from A[i]-1 with an one-step jump
        # OR come from A[i]-2 with a two-step jump
        # So from A[i] rungs, the number of different ways of climbing
        # to the top of the ladder is the Fibonacci number at position
        # A[i] + 1

        result[i] = fib[A[i]+1] & ((1<<B[i])-1)

    return result

A = [4, 4, 5, 5, 1]   
B = [3, 2, 4, 3, 1] 
print(solution(A,B))

#https://codesays.com/2014/solution-to-ladder-by-codility/

