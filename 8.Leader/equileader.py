"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

...

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

        ...
"""

"""
#WRONG SOLUTION ??

from collections import Counter

def solution(A):

    result = 0
    equileader, equil_count = Counter(A).most_common()[0]

    left = 0

    for i, value in enumerate(A):

        if value == equileader:
            left += 1

        if left > (i+1) // 2 and (equil_count - left) > (len(A) - (i + 1)) // 2: 
            result +=1

        return result         
"""        

def solution(A):

    size = len(A)
    count, count1, sequence, answer = 0, 0, 0, 0

    for i in A:
        if 0 == count:
            sequence = i

        if sequence == i:
            count += 1

        else:
            count -= 1

    count = A.count(sequence)

    if count > size // 2:

        for i in xrange(size):

            if A[i] == sequence:
                count1 += 1

            if count1 > (i + 1) // 2 and count - count1 > (size - 1 - i) // 2:
                answer += 1

    return answer


A = [4, 3, 4, 4, 4, 2]
print(solution(A))

#https://codesays.com/2014/solution-to-equi-leader-by-codility/
