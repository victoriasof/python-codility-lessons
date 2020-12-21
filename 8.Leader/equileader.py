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

    length = len(A)
    count1, count2, sequence, result = 0, 0, 0, 0

    for i in A:
        if count1 == 0:
            sequence = i

        if sequence == i:
            count1 += 1

        else:
            count1 -= 1

    count1 = A.count(sequence)

    if count1 > length // 2:

        for i in xrange(length):

            if A[i] == sequence:
                count2 += 1

            if count2 > (i + 1) // 2 and count1-count2 > (length -1 -i) // 2:
                result += 1

    return result


A = [4, 3, 4, 4, 4, 2]
print(solution(A))

#https://codesays.com/2014/solution-to-equi-leader-by-codility/
