"""
This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) 
that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

...
Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
     ...

"""

def solution(A):
    return min(set(range(1, len(A) + 2)) - set(A))
    #return min(set(range(1, len(A) + 2)).difference(set(A)))

A = [1, 3, 6, 4, 1, 2]    
print(solution(A))

#https://www.youtube.com/watch?v=ZNlQ7MnW6sc