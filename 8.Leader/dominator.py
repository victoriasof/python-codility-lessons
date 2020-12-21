"""
An array A consisting of N integers is given. 
The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A 
(namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, 
returns index of any element of array A in which the dominator of A occurs. 
...

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        ...

"""

"""
#FIRST SOLUTION:

from collections import Counter

def solution(A):
    
    if len(A) == 0:
        return -1

    dominator, dom_count = Counter(A).most_common()[0]

    if dom_count <= len(A) // 2:
        return -1

    for i, value in enumerate(A):
        if value == dominator:
            return i    
"""
#SECOND SOLUTION:

def solution(A):

    if len(A) == 0:
        return -1

    sort_a = sorted(A)
    length = len(A) // 2
    dominator = sort_a[length]

    if A.count(dominator) > length:
        return A.index(dominator)
    else:
        return -1    

A = [3, 4, 3, 2, 3, -1, 3, 3]       
print(solution(A))

#function returns index of any element of array A in which the dominator of A occurs. 
#(in this case result is 0)