"""

A positive integer D is a factor of a positive integer N 
if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

    def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, 
because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].

"""

def solution(N):

    count = 1
    result = 0

    while count * count < N:
        # N has two factors: candidate and N // candidate
        if N % count == 0:      
            result += 2
        count += 1

    # If N is square of some value.
    if count * count == N:  
        result += 1

    return result

N = 24    
print(solution(N))

#https://codesays.com/2014/solution-to-count-factors-by-codility/