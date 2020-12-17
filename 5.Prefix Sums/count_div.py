"""
Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] 
that are divisible by K, i.e.:

  ...
For example, for A = 6, B = 11 and K = 2, your function should return 3, 
because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        ...
"""

def solution(A, B, K):

    #count = 0
    #for i in set(range(A, B+1)):
    #    if i % K == 0:
    #        count += 1
    #return count 
    #(correct solution but bad performance)

    #mathematical solution:
    return B // K - (A - 1) // K

A = 6
B = 11
K = 2

print(solution(A,B,K))

#https://stackoverflow.com/questions/34509250/count-div-from-codility-stackoverflowerror-in-program-using-recursion
#https://www.youtube.com/watch?v=G9-E46cj23Y
